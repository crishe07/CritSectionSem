#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:16:08 2023

@author: alumno
"""
from multiprocessing import Process
#from multiprocessing import current_process
from multiprocessing import Value,Lock
import time

N=8

def task(common, tid, lock):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section',flush=True)
        a += 1
        print(f'{tid}−{i}: End of non−critical Section',flush=True )
        lock.acquire()
        
        print(f'{tid}−{i}: Critical section',flush=True)
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section',flush=True)
        time.sleep(0.01)
        common.value = v
        print(f'{tid}−{i}: End of critical section',flush=True)
        lock.release()
        time.sleep(0.01)
        

def main():
    lp = []
    common = Value('i', 0)
    lock=Lock()
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, lock)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")

if __name__ == "__main__":
    main()
