# coding=utf-8

# 查找具体的文件夹,文件名或者文件包含特定字符.
# 如果要查找文件,那个文件夹中不能包含特定字符
# 如果要查找文件夹,那个文件中不能包含特定字符
# 如果要查找的文件夹和文件包含一样的特殊字符,可以使用

import os

dirs = [
    'z:\\AFR',
    'z:\\ANZ',
    'z:\\ASP',
    'z:\\Deadwood',
    'z:\\DOW30',
    'z:\\EUR',
    'z:\\FTSE100',
    'z:\\IPM',
    'z:\\LTA',
    'z:\\NRA',
    'z:\\UKI',
]

# dirs = [
#     'D:\QA\GEDF\GEDataFeed-master\GEDF\MOCAL4169',
#     'D:\QA\GEDF\GEDataFeed-master\GEDF\MOCAL4892'
# ]

specify_daily = 'Daily'
specify_monthly = 'Monthly'
specify_delta = 'Delta'


def process(dir):
    print("开始运行 %s" % dir)
    results = []
    folders = [dir]
    for folder in folders:
        # 把目录下所有文件夹存入待遍历的folders
        folders += [os.path.join(folder, x) for x in os.listdir(folder)
                    if os.path.isdir(os.path.join(folder, x))]

        results += [os.path.relpath(folder, start=dir) # os.path.relpath(os.path.join(folder, x) 这种方式获取文件的路径
                    for x in os.listdir(folder)
                    if os.path.isfile(os.path.join(folder, x))
                    and (specify_daily in x or specify_monthly in x or specify_delta in x)]
    return results


def persistent_data(results):
    print("开始输出")
    set_r = set(results)
    with open('resource/special_path.dat', 'a+') as f:
        for result in set_r:
            f.write(result+"\n")
    for result in set_r:
        print(result)
    print('找到 %s 个结果！' % len(set_r))


for d in dirs:
    rs = process(d)
    persistent_data(rs)