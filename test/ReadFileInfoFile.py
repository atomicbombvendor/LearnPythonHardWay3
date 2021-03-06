# coding=utf-8
# 统计所有利用命令生成的关于文件信息的结果文件.
# 分析出所有的文件的大小和最新的文件的大小
# 文件的路径: D:
# 文件的列表: allDelta.txt allMonthly.txt allDaily.txt
# 把结果保存在同一个结果文件中,一次性写入结果
# 每一行的格式 "Z:\AFR\CorporateAction\CashDividend\Delta\Delta_CashDividend_2017-12-18.zip" 694B 12/19/2017
# "@filePath(space)@fileSizeB(space)@fileLastModifiedDate(space)"
import codecs

from datetime import datetime, date

all_files = [
    'D:\\allDaily.txt',
    'D:\\allMonthly.txt',
    'D:\\allDelta.txt'
]

new_file_date = "2018-04-03."
new_file_date2 = "2018-3."

result_file = "resource/result.dat"

def get_all_size(all_files):
    daily_size = 0
    monthly_size = 0
    delta_size = 0
    daily_new_file_size = 0
    monthly_new_file_size = 0
    delta_new_file_size = 0

    daily_new_file_size2 = 0
    delta_new_file_size2 = 0

    for file in all_files:
        tmp_size = 0
        tmp_new_file_date_size = 0
        tmp_new_file_date_size2 = 0
        with codecs.open(file, 'r', 'utf-8') as f:
            for line in f.readlines():
                if 'GEDF2.0' not in line: # GEDF2.0 是PBFeed的文件夹
                    tmp_date = datetime.strptime(line.strip().split(" ")[2], '%m/%d/%Y')
                    tmp_size += int(line.strip().split(" ")[1][:-1])
                    if new_file_date in line:  # 统计某一天的文件的总的大小
                        tmp_new_file_date_size += int(line.strip().split(" ")[1][:-1])
                    if new_file_date2 in line:  # 统计某一天的文件的总的大小
                        tmp_new_file_date_size += int(line.strip().split(" ")[1][:-1])
                    if tmp_date >= datetime(2018, 1, 31):  # 统计大于某一天的总的大小
                        tmp_new_file_date_size2 += int(line.strip().split(" ")[1][:-1])

        if "Daily" in file:
            daily_size = tmp_size
        elif "Monthly" in file:
            monthly_size = tmp_size
        elif "Delta" in file:
            delta_size = tmp_size
        if "Daily" in file:
            daily_new_file_size = tmp_new_file_date_size
        elif "Monthly" in file:
            monthly_new_file_size = tmp_new_file_date_size
        elif "Delta" in file:
            delta_new_file_size = tmp_new_file_date_size
        if "Daily" in file:
            daily_new_file_size2 = tmp_new_file_date_size2
        elif "Delta" in file:
            delta_new_file_size2 = tmp_new_file_date_size2


    with open(result_file, 'w+') as f:
        tmp = "daily file size>>>" + str(daily_size/(1024**3))+"GB"
        tmp += "\ndelta file size>>>" + str(delta_size/(1024**3))+"GB"
        tmp += "\nmonthly file size>>>" + str(monthly_size/(1024**3))+"GB"
        tmp += "\ndaily_new_file_size 2018-04-05>>>" + str(daily_new_file_size/(1024**3))+"GB"
        tmp += "\nmonthly_new_file_size 2018-04-05>>>" + str(monthly_new_file_size/(1024**3))+"GB"
        tmp += "\ndelta_new_file_size 2018-04-05>>>" + str(delta_new_file_size/(1024**3))+"GB"
        tmp += "\ndelta_new_file_size from 2018-01-31>>>" + str(delta_new_file_size2/(1024**3))+"GB"
        tmp += "\ndaily_new_file_size from 2018-01-31>>>" + str(daily_new_file_size2/(1024**3))+"GB"
        f.write(tmp)
        print("Write Done")

get_all_size(all_files)