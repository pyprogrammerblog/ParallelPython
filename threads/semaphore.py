import threading
import time
import random

semaphore = threading.Semaphore(1)  # by setting one we can start with acquire
# if we want to guarantee that producer start, we can set semaphore initial to zero and remove acquire from producer

# >>> from threading import Semaphore
# >>> sem = Semaphore(5)
# >>> sem._Semaphore__value
# 5
# >>> sem.acquire()
# True
# >>> sem._Semaphore__value
# 4


def consumer():
    print("consumer is waiting.")
    semaphore.acquire()
    print("Consumer notify : consumed item number %s " % item)
    semaphore.release()


def producer():
    semaphore.acquire()
    global item  # <-- global item is busy in this thread, so if someone want it need to be first release
    time.sleep(2)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    item = random.randint(0, 1000)
    print("producer notify : product item number %s" % item)
    semaphore.release()


# Main program
if __name__ == '__main__':
    for i in range(3):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print('finishing {0}th cycle'.format(i))
    print("program terminated")

#
# def consumer():
#     print("consumer is waiting.")
#     semaphore.acquire()
#     print("Consumer notify : consumed item number %s " % item)
#
#
# def producer():
#     global item  # <-- global item is busy in this thread, so if someone want it need to be first release
#     time.sleep(2)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     item = random.randint(0, 1000)
#     print("producer notify : product item number %s" % item)
#     semaphore.release()
#
#
# # Main program
# if __name__ == '__main__':
#     for i in range(3):
#         t1 = threading.Thread(target=producer)
#         t2 = threading.Thread(target=consumer)
#         t1.start()
#         t2.start()
#         t1.join()
#         t2.join()
#         print('finishing {0}th cycle'.format(i))
#     print("program terminated")
