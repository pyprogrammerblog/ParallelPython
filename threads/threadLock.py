import threading

shared_resource_with_lock = 0
shared_resource_without_lock = 0

COUNT = 10000
shared_resource_lock = threading.Lock()

#  Acquire and release are in charge of giving access to the shared resource
#  When a resource is not available acquire waits till is available.


def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


def increment_without_lock():
    global shared_resource_without_lock
    for i in range(COUNT):
        shared_resource_without_lock += 1


def decrement_without_lock():
    global shared_resource_without_lock
    for i in range(COUNT):
        shared_resource_without_lock -= 1


def main():
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print('value with lock ' + str(shared_resource_with_lock))
    print('value without lock ' + str(shared_resource_without_lock))


if __name__ == "__main__":
    main()
