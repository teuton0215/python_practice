#/use/env/python 3
#-*- encoding:utf-8 -*-
from multiprocessing import  Pool
import  os, time, random

def long_time_tash(name):
    print("Run task %s (%s)..."% (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end =time.time()
    print('Task %s runs %0.2f second.'% (name,(end - start)))

if __name__ =='__main__':
    print("Parent process %s." % os.getpid())
    p = Pool(4)
    for i in range(5):
            p.apply_async(long_time_tash,args=(i,))
    print('Waiting for all subprocesses done....')
    p.close()
    p.join()
    print('All subprocesses done')
