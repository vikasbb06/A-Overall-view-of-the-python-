from threading import Thread,Lock
import time
#lock is used to prevent the race condition & has 2 function acquire,release
database_value=0
def increase(lock):
    global database_value
    lock.acquire()  # we can also use with lock:,Then lock.release is not necessary
    local_copy=database_value

    #processing & analysing of the race condition
    local_copy+=1
    time.sleep(0.1)
    database_value=local_copy
    lock.release()

if __name__=="__main__":
    lock=Lock()
    print("Start Value of database:",database_value)
    
    thread1=Thread(target=increase,args=(lock,)) 
    thread2=Thread(target=increase,args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End Value of the database:",database_value) # output is 1 to prevent this we use the lock object