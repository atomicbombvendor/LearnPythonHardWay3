# 多进程
# coding=utf-8

import multiprocessing
import os



def run_proc(name):
    print('Child process {0} {1} Running'.format(name, os.getpid()))

def run_proc2(msg):
    print(multiprocessing.current_process().name + '-' + msg)

# if __name__ == '__main__':
#     print('Parent process {0} is Running'.format(os.getpid()))
#     for i in range(5):
#         p = multiprocessing.Process(target=run_proc, args=(str(i)))
#         print("process start")
#         p.start() # 这里建立了5个单独的子进程.
#     p.join()
#     print("Process close")

# if __name__ == "__main__":
#     pool = multiprocessing.Pool()
#     for i in range(10):
#         msg = "hello %d" % i
#         pool.apply_async(run_proc2, (msg,))
#     pool.close()  # 关闭进程池，表示不能再往进程池中添加进程，需要在join之前调用
#     pool.join() # 等待进程池中的所有进程执行完毕
#     print("Sub-process(es) done")
