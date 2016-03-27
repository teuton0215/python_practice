#/use/env/python 3
#-*- encoding:utf-8 -*-
from  multiprocessing import  Process
import os
#The child process to execute code
def run_proc(name):
    print('Run child process %s (%s)...'% (name, os.getpid()))

if  __name__=='__main__':
    #get parent process ID
    print('Parent process %s.'% os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')