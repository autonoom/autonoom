from CU import CU

#!/usr/bin/python
#https://www.tutorialspoint.com/python/python_multithreading.htmhttps://www.tutorialspoint.com/python/python_multithreading.htm
import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        run2()
        print "kak kip"

def main():
    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()



def run2():
    cu= CU()
    cu.Checkvalue()


main()




