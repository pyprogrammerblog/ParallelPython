from threading import Thread


def my_function(x):
    print('my function is printing: ' + str(x))
    return None

threads = []
for x in range(5):
    t = Thread(target=my_function, args=(x, ))
    print('starting')
    t.start()
    print('already started and finished')
    threads.append(t)
    t.join()
    print('joined to original thread')

print('#########################')
print(threads)