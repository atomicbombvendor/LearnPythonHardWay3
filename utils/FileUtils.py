# coding=utf-8
import codecs
import os


# Root:根目录,获取此目录下的所有文件
# str_old: 要替换的字符串
# str_new: 新的字符串
class FileUtils:

    # 获取文件夹下所有的文件路径
    def getAllFiles(self, root):
        file_Path = []
        for root, dirs, files in os.walk(root, topdown=False):
            # print "root -> ", root
            for filef in files:
                file_Path.append(os.path.join(root, filef))

        return file_Path


f = FileUtils()
print("Start")
file_path = f.getAllFiles("D:\QA\GEDF\GeDataFeed-MOCAL4936\GEDF")
print("Print all path>>>>>>>")
for file in file_path:
    if 'ctrl' not in file:
        print(file)
print("Done!")

# print "Process 201803"
# not_match_201803 = []
# for file in file_path:
#     if 'ctrl' not in file:
#         if '\Fundamental\\' in file:
#             not_match_201803.append(file)
#             print file
#         elif '_GeneralProfile_' in file or '_GeneralProfileCombined_' in file:
#             not_match_201803.append(file)
#             print file



