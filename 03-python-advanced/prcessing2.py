from multiprocessing import Process,Value,Array,Lock
import time
# to avoid race condition we use lock 
def add_100(number,lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        number.value+=1
        lock.release()
        
if __name__=="__main__":
    lock=Lock()
    shared_number= Value('i',0)
    print("Number at beginning: ",shared_number.value)

    p1=Process(target=add_100,args=(shared_number,lock))
    p2=Process(target=add_100,args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("number at Ending: ",shared_number.value) #race condition





