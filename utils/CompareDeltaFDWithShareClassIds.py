# coding=utf-8
# 根据CompanyId的列表找到其中一个Region的文件,进行全量的对比
# 文件来自Dev的文件夹和Live的文件夹
# Dev文件夹路径 \\morningstar.com\shares\GeDataFeed\GeDataFeed\DEV\PT2.0_GEDF_180315
# 比较的文件的日期应该是0324的
# Live文件夹路径 \\morningstar.com\shares\GeDataFeed\GeDataFeed
# 对比的文件是:
# EarningReport AOR/Restate
# Fundamental AOR/Restate
# EarningRatio AOR/Restate
# OperationRatio AOR/Restate
# 每一个Id要比较8个文件.
# 把结果按照 {FileType}_{AOR|Restate}_{Region}_{CompanyId}\{Data_Only_In_0324.dat|Data_Only_In_0402.dat}
import codecs
import os
import zipfile


class CompareFile:

    def __init__(self):
        self.z_path = "\\\\morningstar.com\shares\GeDataFeed\GeDataFeed"
        self.dev_path = "z:\DEV\PT2.0_GEDF_180315"
        self.live_path = "z:\\"
        self.file_names = [  # dev的文件已经指定了日期{2018-03-24}; live的应该是0402
            '@Region@\Fundamental\FinancialStatements\Delta\Delta_FinancialStatementsAOR_@Date@.zip',
            '@Region@\Fundamental\FinancialStatements\Delta\Delta_FinancialStatementsRestate_@Date@.zip',
            # '@Region@\Fundamental\EarningRatios\Delta\Delta_EarningRatiosAOR_@Date@.zip',
            # '@Region@\Fundamental\EarningRatios\Delta\Delta_EarningRatiosRestate_@Date@.zip',
            # '@Region@\Fundamental\EarningReports\Delta\Delta_EarningReportsAOR_@Date@.zip',
            # '@Region@\Fundamental\EarningReports\Delta\Delta_EarningReportsRestate_@Date@.zip',
            '@Region@\Fundamental\OperationRatios\Delta\Delta_OperationRatiosAOR_@Date@.zip',
            '@Region@\Fundamental\OperationRatios\Delta\Delta_OperationRatiosRestate_@Date@.zip'
        ]  # EarningReport和EarningRatios是ShareClassId,怎么做?
        self.dev_date = '2018-03-24'
        self.live_date = '2018-03-29'
        self.log_file = "../log/compare_delta_log.txt"
        self.result_file_path = "D:\QA\GEDF\GeDataFed-0402\@CompanyId@_@File@_@Region@"

    def start_compare_file_with_companyId(self, config_file):
        with codecs.open(self.log_file, 'w+', 'utf-8') as fnd: pass
        id_regions = self.read_config_file(config_file)
        for data in id_regions:
            companyId = data.strip().split("|")[0]
            region = data.strip().split("|")[1]
            for fname in self.file_names:

                self.write_log("Start Process>> CompanyId: %s, File:%s" % (companyId, self.get_file_name(fname, region, self.dev_date)[:-15]))
                print("Start Process>> CompanyId: %s, File:%s" % (companyId, self.get_file_name(fname, region, self.dev_date)[:-15]))

                result_path = self.get_result_file_path(region=region, companyId=companyId, file_name=fname)

                dev_file_path = os.path.join(self.dev_path, self.get_file_name(fname, region, self.dev_date))
                live_file_path = os.path.join(self.live_path, self.get_file_name(fname, region, self.live_date))
                data_0324 = self.get_data_from_zip(file=dev_file_path, companyId=companyId)
                data_0402 = self.get_data_from_zip(file=live_file_path, companyId=companyId)

                if (not data_0324) and (not data_0402):  # 两个都为空
                    self.write_log(data="Can't find %s in %s\r\nCan't find %s in %s\r\n" % (companyId, dev_file_path, companyId, live_file_path))
                    print("Can't find %s in %s\r\nCan't find %s in %s\r\n" % (companyId, dev_file_path, companyId, live_file_path))
                else:
                    self.compare_file(result_path, data_0324, data_0402)

                self.write_log("Process Done\r\n")
                print("Process Done\r\n")

    # 传入两个参数,file_name是带日期占位符的文件名, date是需要填充占位符的值,格式应该是YYYY-MM-DD
    @staticmethod
    def get_file_name(file_name, region, date):
        return file_name.replace('@Date@', date).replace('@Region@', region)

    # 读取配置文件的每一行放入列表
    @staticmethod
    def read_config_file(config_file):
        datas = []
        with open(config_file, 'r') as f:
            for line in f.readlines():
                datas.append(line)
        return datas

    # 比较文件的内容,data_0324和data_0402是从压缩包中的文件读取出来的内容
    # 把结果存入 path路径下的两个文件
    def compare_file(self, path, data_0324, data_0402):
        result_0324 = path + '\Data_Only_In_0324.dat'
        result_0402 = path + '\Data_Only_In_0402.dat'
        set_data_0324 = None
        set_data_0402 = None
        if data_0324:
            set_data_0324 = self.get_data_set(data_0324)
        else:
            self.write_log("data_0324 is none")
            print("data_0324 is none")

        if data_0402:
            set_data_0402 = self.get_data_set(data_0402)
        else:
            self.write_log("set_data_0402 is none")
            print("set_data_0402 is none")
        data_only_in_0324, data_only_in_0402 = self.compare_set(set_data_0324, set_data_0402)
        self.write_file(data_only_in_0324, data_only_in_0402, path, result_0324, result_0402)

    # 比较两个Set，返回比较结果
    @staticmethod
    def compare_set(data1, data2):
        sd = set(data1) if data1 else set()
        sl = set(data2) if data2 else set()
        return sd - sl, sl - sd

    # 把从文件中读取到的数据的每一行作为Set的一个元素.
    @staticmethod
    def get_data_set(data):
        result = set()
        if data is None:
            return result
        lines = data.split('\r\n')
        for line in lines:
            result.add(line)
        return result

    # 将不同写入文件
    # data1, data2
    # path 存放结果的文件夹路径
    # 存放结果的文件名 data1_result_file, data2_result_file
    @staticmethod
    def write_file(data1, data2, path, data1_result_file, data2_result_file):
        if not os.path.exists(path):
            os.makedirs(path)  # 创建级联目录
        with codecs.open(data1_result_file, 'w', 'utf-8') as fnl:
            for line in list(data1):
                fnl.write(str(line) + "\r\n")
        with codecs.open(data2_result_file, 'w', 'utf-8') as fnd:
            for line in list(data2):
                fnd.write(str(line) + "\r\n")

    # 读取压缩包里面的文件具体CompanyId的文件
    def get_data_from_zip(self, file, companyId):
        if not os.path.exists(file):
            print('zip file not found: ' + file.replace("z:", self.z_path))
            self.write_log("zip file not found: " + file.replace("z:", self.z_path))
            return False
        zfile = zipfile.ZipFile(file, 'r')
        data = ''
        for filename in zfile.namelist():
            if companyId in filename:
                data += str(zfile.read(filename), 'utf-8')
        return data

    def write_log(self, data):
        with codecs.open(self.log_file, 'a+', 'utf-8') as fnd:
                fnd.write(str(data)+"\r\n")

    def get_result_file_path(self, region, companyId, file_name):
        fname = ''
        if "EarningReportsAOR" in file_name:
            fname = "EarningReportsAOR"
        if "EarningReportsRestate" in file_name:
            fname = "EarningReportsRestate"
        if "EarningRatiosAOR" in file_name:
            fname = "EarningRatiosAOR"
        if "EarningRatiosRestate" in file_name:
            fname = "EarningRatiosRestate"
        if "FinancialStatementsAOR" in file_name:
            fname = "FinancialStatementsAOR"
        if "FinancialStatementsRestate" in file_name:
            fname = "FinancialStatementsRestate"
        if "OperationRatiosAOR" in file_name:
            fname = "OperationRatiosAOR"
        if "OperationRatiosRestate" in file_name:
            fname = "OperationRatiosRestate"
        return self.result_file_path.replace('@Region@', region).replace('@CompanyId@', companyId).replace('@File@', fname)


# 开始运行
RC = CompareFile()
RC.start_compare_file_with_companyId("CompanyIds.txt")