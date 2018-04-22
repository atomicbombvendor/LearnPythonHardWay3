import queue
import threading
import time

exit_flag = 0

class myThread2(threading.Thread):

    def __init__(self, threadId, name, q):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.q = q

    def run(self):
        print("Start" + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)

def process_data(thread_name, q):
    while not exit_flag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (thread_name, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['One', 'two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = queue.Queue(10) # FIFO
threads = []
threadId = 1

for t_name in threadList:
    thread = myThread2(threadId, t_name, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exit_flag = 1

# 三个线程争夺五个资源,每次从队列中取出后,队列中就没有这个资源了.
for t in threads:
    t.join()
print("Exiting Main Thread")
