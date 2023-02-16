"""
Created on Thu Feb 16 09:16:08 2023

@author: alumno
"""
from multiprocessing import Process
from multiprocessing import Value,BoundedSemaphore
import time

N=8
def task(common, tid, bs):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        bs.acquire()
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        #time.sleep(0.01)
        common.value = v
        print(f'{tid}−{i}: End of critical section')
        bs.release()

def main():
    lp = []
    common = Value('i', 0)
    bs=BoundedSemaphore()
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, bs)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")

if __name__ == "__main__":
    main()
