#import threading
from threading import current_thread, Thread
print("Program started ",current_thread().name)

def odds():
    for i in range(1, 21, 2):
        print(i, current_thread().name)

def evens():
    for i in range(2, 21, 2):
        print(i, current_thread().name)


thread1 = Thread(target=odds)
thread2 = Thread(target=evens)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
