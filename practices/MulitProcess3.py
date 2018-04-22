# coding=utf-8
import multiprocessing
import time
import os

# 测试主进程和子进程支架的信息共享

data_list = ['++++']


def add_data():
    global data_list
    data_list.append(1)
    data_list.append(2)
    data_list.append(3)
    print("子进程", os.getpid(), data_list)


if __name__ == '__main__':
    p = multiprocessing.Process(target=add_data, args=())
    p = multiprocessing.Value("d", 10)
    p.start()
    p.join()
    data_list.append("a")
    data_list.append("b")
    data_list.append("c")

    print("主进程", os.getpid(), data_list)
