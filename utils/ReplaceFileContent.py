# coding=utf-8
import codecs
import os


# Root:根目录,获取此目录下的所有文件
# str_old: 要替换的字符串
# str_new: 新的字符串
class ReplaceFileContent:

    def __init__(self):
        self.root = "D:\QA\GEDF\GeDataFeed-MOCAL4937\TestCase"
        self.file_paths = []
        self.str_old = r"\\morningstar.com\shares\GeDataFeed\GeDataFeed\FTSE100"
        self.str_new = r"D:\QA\GEDF\GeDataFeed-MOCAL4937\GEDF\FTSE100"

    def setRoot(self, root):
        self.root = root

    def setStrOld(self, str_old):
        self.str_old = str_old

    def setStrNew(self, str_new):
        self.str_new = str_new

    # os.path.walk得到文件夹上面的所有文件，不包括目录
    def getAllFiles(self):
        os.path.walk(self.root, self.processDirectory, None)

    # getAllFiles的回调函数，用于向file_paths数组赋值
    def processDirectory(self, args, dirname, filenames):
        for filename in filenames:
            filef = os.path.join(dirname, filename)
            if not os.path.isdir(filef):
                self.file_paths.append(filef)

    # os.walk非递归的方式获取所有的文件路径。
    def getAllFiles2(self):
        for root, dirs, files in os.walk(self.root, topdown=False):
            for filef in files:
                self.file_paths.append(os.path.join(root, filef))

    # 替换文件的内容，全局的。
    def replaceContent(self, file):
        file_data = ""
        with codecs.open(file, 'r', 'utf-8') as f:  # w会清空原来的内容 a为追加
            for line in f.readlines():
                file_data += line.replace(self.str_old, self.str_new)
            self.writeFile(file, file_data)

    @staticmethod
    def writeFile(file, data):
        f = codecs.open(file, 'w', 'utf-8')  # w会清空原来的内容 a为追加
        f.write(str(data))
        f.close()

    # 全局替换文件内容
    def replaceAllFileContent(self):
        self.getAllFiles2()
        for f in self.file_paths:
            self.replaceContent(f)
        print("Replace Done")


R = ReplaceFileContent()
R.setRoot("D:\QA\GEDF\GEDataFeed-master\TestCase-4892")

R.setStrNew(r"/ZipFilesDir=D:\QA\GEDF\GEDataFeed-master\GEDF\MOCAL4892")
R.setStrOld(r"/ZipFilesDir=D:\QA\GEDF\GeDataFeed-master\GEDF")
R.replaceAllFileContent()

R.setStrOld(r"D:\GEDataFeed\GeDataFeed_Monthly\bin\EquityDataFeed.exe")
R.setStrNew(r"D:\QA\GEDF\GeDataFeed-MOCAL4892\GeDataFeed_Monthly\bin\EquityDataFeed.exe")
R.replaceAllFileContent()

R.setStrOld(r"D:\GEDataFeed\GeDataFeed_Delta\bin\EquityDataFeed.exe")
R.setStrNew(r"D:\QA\GEDF\GeDataFeed-MOCAL4892\GeDataFeed_Delta\bin\EquityDataFeed.exe")
R.replaceAllFileContent()

R.setStrOld(r"/ZipFilesDir=\\morningstar.com\shares\GeDataFeed\GeDataFeed")
R.setStrNew(r"/ZipFilesDir=D:\QA\GEDF\GeDataFeed-MOCAL4892\GEDF")
R.replaceAllFileContent()

R.setStrOld(r"/TargetFileDate=%1")
R.setStrNew(r"/TargetFileDate=2018-03-22")
R.replaceAllFileContent()



# R.setStrOld(r"/ZipFilesDir=\\morningstar.com\shares\GeDataFeed\GeDataFeed")
# R.setStrNew(r"/ZipFilesDir=D:\QA\GEDF\GeDataFeed-MOCAL4936\GEDF")
# R.replaceAllFileContent()




