from threading import Thread, Condition
import time

items = []
condition = Condition()


class consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(2):
            time.sleep(6)
            # When consumer is executing, producer is waiting for Lock
            self.consume()

    def consume(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 0:  # <-- if list has more than one element, notify is pointless, it will keep running
            condition.wait()  # <-- if list has 0 element, we need to wait for notify (all) for jump this barrier
            print("Consumer notify : no item to consume")
        items.pop()  # <-- this is a list method ()
        #  list.append(x)
        #  list.insert(i, x)
        #  list.remove(x)
        print("Consumer notify : consumed 1 item")
        print("Consumer notify : items to consume are " + str(len(items)))
        condition.notify()  # <-- Notify after removing just in case buffer of production is full
        condition.release()


class producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(2):
            time.sleep(2)
            # When producer is executing, consumer is waiting for Lock
            self.produce()

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("Producer notify : items producted are " + str(len(items)))
            print("Producer notify : stop the production!!")
        items.append(1)
        print("Producer notify : total items producted " + str(len(items)))
        condition.notify()
        condition.release()


if __name__ == "__main__":
    producer = producer()
    consumer = consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print(items)
