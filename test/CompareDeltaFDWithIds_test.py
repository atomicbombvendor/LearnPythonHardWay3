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

import self as self


class CompareFile:

    def __init__(self):
        self.z_path = "\\\\morningstar.com\shares\GeDataFeed\GeDataFeed"
        self.dev_path = "z:\DEV\PT2.0-GEDF-20180324"
        self.live_path = "z:\\" # z:\\
        self.file_name_companyId = [
            '@Region@\Fundamental\FinancialStatements\Delta\Delta_FinancialStatementsAOR_@Date@.zip',
            '@Region@\Fundamental\FinancialStatements\Delta\Delta_FinancialStatementsRestate_@Date@.zip',
            '@Region@\Fundamental\OperationRatios\Delta\Delta_OperationRatiosAOR_@Date@.zip'
            '@Region@\Fundamental\OperationRatios\Delta\Delta_OperationRatiosRestate_@Date@.zip'
        ]

        self.file_name_shareClassId = [
            '@Region@\Fundamental\EarningRatios\Delta\Delta_EarningRatiosAOR_@Date@.zip',
            '@Region@\Fundamental\EarningRatios\Delta\Delta_EarningRatiosRestate_@Date@.zip',
            '@Region@\Fundamental\EarningReports\Delta\Delta_EarningReportsAOR_@Date@.zip',
            '@Region@\Fundamental\EarningReports\Delta\Delta_EarningReportsRestate_@Date@.zip'
        ]
        self.dev_date = '2018-2'
        self.live_date = '2018-04-02' # 2018-04-02
        self.log_file = "../log/compare_delta_log.txt"
        # self.log_file_companyId = "../log/compare_delta_log_companyId.txt"
        self.result_file_path_companyId = "D:\QA\GEDF\GeDataFed-test\CompanyId_test\@CompanyId@_@File@_@Region@"
        # self.log_file_shareClassId = "../log/compare_delta_log_shareClassId.txt"
        self.result_file_path_shareClassId = "D:\QA\GEDF\GeDataFed-test\ShareClassId_test\@CompanyId@_@ShareClassId@_@File@_@Region@"
    
    def set_log_file(self, log_file):
        self.log_file = log_file

    def get_log_file(self):
        return self.log_file
    
    def start_compare_file_with_companyId(self, config_file):
        id_regions = self.read_config_file(config_file)
        for data in id_regions:
            companyId = data.strip().split("|")[0]
            region = data.strip().split("|")[1]
            for fname in self.file_name_companyId:

                self.write_log("Start Process>> CompanyId: %s, File:%s.zip"
                               % (companyId, self.get_file_name(fname, region, self.dev_date)[:-15]))
                print("Start Process>> CompanyId: %s, File:%s.zip"
                      % (companyId, self.get_file_name(fname, region, self.dev_date)[:-15]))

                result_path = self.get_result_file_path(region=region, companyId=companyId, file_name=fname)

                dev_file_path = os.path.join(self.dev_path, self.get_monthly_file_name(fname, region, self.dev_date))
                live_file_path = os.path.join(self.live_path, self.get_file_name(fname, region, self.live_date))
                data_0324 = self.get_data_from_zip(file=dev_file_path, id=companyId)
                data_0402 = self.get_data_from_zip(file=live_file_path, id=companyId)

                if (not data_0324) and (not data_0402):  # 两个都为空
                    self.write_log(data="Both File Can't find {%s in %s} and {%s in %s}\r\n"
                                        % (companyId, dev_file_path, companyId, live_file_path))
                    print("Both File Can't find {%s in %s} and {%s in %s}\r\n"
                          % (companyId, dev_file_path, companyId, live_file_path))
                    self.compare_file(result_path, data_0324, data_0402, 1)
                else:
                    self.compare_file(result_path, data_0324, data_0402)

                self.write_log("Process Done\r\n")
                print("Process Done\r\n")

    def start_compare_file_with_shareclassId(self, config_file):
        id_regions = self.read_config_file(config_file)
        for data in id_regions:
            companyId = data.strip().split("|")[0]
            shareclassId = data.strip().split("|")[1]
            region = data.strip().split("|")[2]
            for fname in self.file_name_shareClassId:

                self.write_log("Start Process>> CompanyId: %s, ShareClassId: %s, File:%s.zip"
                               % (companyId, shareclassId, self.get_file_name(fname, region, self.dev_date)[:-15]))
                print("Start Process>> CompanyId: %s, ShareClassId: %s, File:%s.zip"
                      % (companyId, shareclassId, self.get_file_name(fname, region, self.dev_date)[:-15]))

                result_path = self.get_result_file_path(region=region, companyId=companyId,
                                                        shareClassId=shareclassId, file_name=fname)

                dev_file_path = os.path.join(self.dev_path, self.get_monthly_file_name(fname, region, self.dev_date))
                live_file_path = os.path.join(self.live_path, self.get_file_name(fname, region, self.live_date))
                data_0324 = self.get_data_from_zip(file=dev_file_path, id=shareclassId)
                data_0402 = self.get_data_from_zip(file=live_file_path, id=shareclassId)

                if (not data_0324) and (not data_0402):  # 两个都为空
                    self.write_log(data="Can't find %s|%s in %s\r\nCan't find %s|%s in %s\r\n"
                                        % (companyId, shareclassId, dev_file_path, companyId, shareclassId, live_file_path))
                    print("Can't find %s|%s in %s\r\nCan't find %s|%s in %s\r\n"
                          % (companyId, shareclassId, dev_file_path, companyId, shareclassId, live_file_path))
                else:
                    self.compare_file(result_path, data_0324, data_0402)

                self.write_log("Process Done\r\n")
                print("Process Done\r\n")

    # 传入两个参数,file_name是带日期占位符的文件名, date是需要填充占位符的值,格式应该是YYYY-MM-DD
    @staticmethod
    def get_file_name(file_name, region, date):
        return file_name.replace('@Date@', date).replace('@Region@', region)

    # 需要比较的是Monthly的文件,所以要把原来Delta的zip文件转换为Monthly的文件名
    # 格式 {@Region@}_Monthly_{@FileType@}_{@Date@}.zip
    @staticmethod
    def get_monthly_file_name(file_name, region, date):
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

        pattern = "@Region@_Monthly_@FileType@_@Date@.zip"
        return pattern.replace("@Region@", region)\
                .replace("@FileType@", fname)\
                .replace("@Date@", date)

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
    # flag=0,没有不同的地方; flag=1表示两边的文件都找不到
    def compare_file(self, path, data_0324, data_0402, flag=0):
        result_0324 = path + '\Data_Only_In_0324.dat'
        result_0402 = path + '\Data_Only_In_0402.dat'
        set_data_0324 = None
        set_data_0402 = None
        if data_0324:
            set_data_0324 = self.get_data_set(data_0324.strip())
        else:
            self.write_log("data file is not exits which generate at 03/24")
            print("data file is not exits which generate at 03/24")

        if data_0402:
            set_data_0402 = self.get_data_set(data_0402.strip())
        else:
            self.write_log("data file is not exits which generate at 04/02")
            print("data file is not exits which generate at 04/02")
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

    # 将比较的结果写入文件
    # data1, data2
    # path 存放结果的文件夹路径
    # 存放结果的文件名 data1_result_file, data2_result_file
    def write_file(self, data1, data2, path, data1_result_file, data2_result_file):

        # 同时为空的,表示没有不相同的.不生成文件
        if not len(data1) and not len(data2) :
            print("No diff")
            self.write_log("No diff")
            return
        print("Have diff")
        self.write_log("Have diff")
        if not os.path.exists(path):
            os.makedirs(path)  # 创建级联目录

        with codecs.open(data1_result_file, 'w', 'utf-8') as fnl:
            for line in self.order_list(data1):
                fnl.write(str(line) + "\r\n")

        with codecs.open(data2_result_file, 'w', 'utf-8') as fnd:
            for line in self.order_list(data2):
                fnd.write(str(line) + "\r\n")

    # 传入set, 然后把set转为List,并排序.返回List
    def order_list(self, data):
        list_data = list(data)
        return sorted(list_data, key=lambda x: self.cmp(x))

    def cmp(self, key):
        values = key.split("|")
        return str(values[0]+values[1]+str(values[3:]))

    # 读取压缩包里面的文件具体CompanyId的文件
    def get_data_from_zip(self, file, id):
        if not os.path.exists(file):
            print('zip file not found: ' + file.replace("z:", self.z_path))
            self.write_log("zip file not found: " + file.replace("z:", self.z_path))
            return False
        zfile = zipfile.ZipFile(file, 'r')
        data = ''
        for filename in zfile.namelist():
            if id in filename:
                data += str(zfile.read(filename), 'utf-8')
        return data

    def write_log(self, data):
        with codecs.open(self.log_file, 'a+', 'utf-8') as fnd:
                fnd.write(str(data)+"\r\n")

    def get_result_file_path(self, region, companyId, file_name, shareClassId=None):
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
        if not shareClassId:
            return self.result_file_path_companyId\
                .replace('@Region@', region)\
                .replace('@CompanyId@', companyId)\
                .replace('@File@', fname)
        else:
            return self.result_file_path_shareClassId.replace('@Region@', region) \
                .replace('@CompanyId@', companyId) \
                .replace('@File@', fname) \
                .replace('@ShareClassId@', shareClassId)


# 开始运行
RC = CompareFile()
company_log_file = "../log/compare_delta_log_companyId_test.txt"
shareClass_log_file = "../log/compare_delta_log_shareClassId_test.txt"

RC.set_log_file(company_log_file)
# RC.set_log_file(shareClass_log_file)

with codecs.open(RC.get_log_file(), 'w+', 'utf-8') as fnd: pass

RC.write_log("Compare file that is generated at 03/24 with file generated at 04/02")
RC.write_log("File's path is share folder\DEV\PT2.0-GEDF-20180324 which generated at 03/24")
RC.write_log("File's path is share folder\ which generated at 04/02")
RC.write_log("Share folder is \\\\morningstar.com\shares\GeDataFeed\GeDataFeed\n")

RC.start_compare_file_with_companyId("CompanyIds_test.txt")
# RC.start_compare_file_with_shareclassId("ShareClassIds.txt")