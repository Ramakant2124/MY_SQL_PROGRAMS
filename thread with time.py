import threading
import time

print(" Main Program Stared")

def greet(name):
    print('Good Morning',name)

name="Ramakant"
t1=threading.Thread(target=greet,args=(name,))
t1.start()
t1.join()

print("Both Threads Finished. Main Program End.")
