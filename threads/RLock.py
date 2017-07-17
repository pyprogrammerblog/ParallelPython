import threading
import time


class Box(object):
    """Box class"""

    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def adder(self, n):
        Box.lock.acquire()
        self.execute(n)  # <-- Execute executes when Lock is acquired. Execute is a different function share by
        #  different threads, so in order to acquire inside of acquire we need a recursive Lock
        Box.lock.release()


def my_function(obj, items):
    while items > 0:
        print('adding 1 item per cycle')
        obj.adder(items)
        time.sleep(1)
        items -= 1


def main():
    """ Main """

    box = Box()
    t1 = threading.Thread(target=my_function, args=(box, 6))
    t1.start()
    t1.join()

    print(box.total_items)

if __name__ == "__main__":
    main()
