# threading for python
import threading

add threads: 
added_thread = threading.Thread(target = func, args=(args*))

finish threads after the main function:
added_thread.join()

thread lock for sharing variance:
def func1(args*,):

  global sharing variance, lock
  lock.acquire()
  code *** body
  lock.release()

def func2(args*,):

  global sharing variance, lock
  lock.acquire()
  code *** body
  lock.release()

sharing variance, lock = 0, threading.Lock()
added_thread1 = threading.Thread(target = func1, args=(args*))
added_thread2 = threading.Thread(target = func2, args=(args*))

