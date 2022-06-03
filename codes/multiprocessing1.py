# what is multiprocessing? 
# multiprocessing refers to the ability of a system to support
# more than one processor at the same time

from multiprocessing import Process, Queue
import multiprocessing
# process

def f(name):
    print("hello {}".format(name))
    new = name + '_done!'
    return new

def f2():
    for i in range(0, 100):
        print(i)
    return "counted all"

if __name__ == '__main__':
    q = Queue()
    
    p1 = Process(target = f, args=('bob',))
    p2 = Process(target = f2)
    p3 = Process(target = f2)
    p4 = Process(target = f, args = ('sally',))
    
    p1.start()
    p2.start()
    p4.start()
    p3.start()
    
    p3.join()
    p1.join()
    p2.join()
    p4.join()
    

