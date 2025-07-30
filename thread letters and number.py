from threading import current_thread,Thread

def letters():
    for i in range(ord('a'),ord('z')+1):
        print(chr(i))

def number():
    for i in range(1,26):
        print(i)

thread1 = Thread(target=letters)
thread2 = Thread(target=number)
        
thread1.start()
thread2.start()
