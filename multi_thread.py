"""
python多线程
"""
import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(5)
        count += 1
        print("%s:%s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("Thread-1", 2))
    _thread.start_new_thread(print_time, ("Thread-2", 5))

except:
    print('无法启动线程')


