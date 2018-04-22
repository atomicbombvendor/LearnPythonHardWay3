from multiprocessing import Pool
import time


def task(msg, msg2):
    print('hello, %s, %s' % (msg, msg2))
    time.sleep(1)


if __name__ == '__main__':
    pool = Pool(processes=4)

    for x in range(10):
        pool.apply_async(task, args=(x, x+1,))

    pool.close()
    pool.join()

    print('processes done.')