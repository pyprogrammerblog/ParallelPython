import threading
import time


def my_funt_1():
    print(threading.current_thread().getName() + ' is starting now \n')
    time.sleep(3)
    print(threading.current_thread().getName() + ' is exiting \n')


def my_funt_2():
    print(threading.current_thread().getName() + ' is starting now \n')
    time.sleep(3)
    print(threading.current_thread().getName() + ' is exiting \n')


def my_funt_3():
    print(threading.current_thread().getName() + ' is starting now \n')
    time.sleep(3)
    print(threading.current_thread().getName() + ' is exiting \n')


def main():

    print('starting main thread')

    t1 = threading.Thread(target=my_funt_1, name='function 1')
    t2 = threading.Thread(target=my_funt_2, name='function 2')
    t3 = threading.Thread(target=my_funt_3, name='function 3')

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print('exiting main thread')

if __name__ == "__main__":
    main()
