import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello $s (in %s)', std, threading.current_thread().name)


def runningThread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=runningThread, args=('Alice',), name='Thread1')
t2 = threading.Thread(target=runningThread, args=('George',), name='Thread2')
t1.start()
t2.start()
t1.join()
t2.join()
