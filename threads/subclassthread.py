import threading
import time

exit_flag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        super(MyThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting ' + self.name + '\n')
        my_function(self.name, 2, self.counter)
        print('Exiting ' + self.name + '\n')

    # function could be inside of class and be called self.my_...


def my_function(threadName, delay, counter):
    while counter:
        if exit_flag:
            thread.exit()
            # break
        time.sleep(delay)
        print('{0}: {1}'.format(threadName, time.ctime(time.time())))
        counter -= 1


def main():
    """ Main """
    thread1 = MyThread(1, "Thread - 1", 5)
    thread2 = MyThread(2, "Thread - 2", 3)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end program')

if __name__ == '__main__':
    main()
