from multiprocessing import Process, Event
import time

def task1(e, msg):
    print('task1 is waitting')
    e.wait()
    time.sleep(1)
    print('hello, {0}, e.is_set(): {1}'.format(msg, e.is_set()))

def task2(e, msg):
    print('task2 is waitting')
    e.wait(msg)
    print('hello, {0}, e.is_set(): {1}'.format(msg, e.is_set()))

if __name__ == '__main__':
    e = Event()

    p1 = Process(target=task1, args=(e, 1))
    p2 = Process(target=task2, args=(e, 2))

    p1.start()
    p2.start()

    time.sleep(3)

    e.set()
    print('main: event is set')