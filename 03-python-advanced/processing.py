from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        i*i

if __name__=="__main__":
    processs=[]
    num_processes=os.cpu_count()
    #number of CPUs on the machine.Usually a good choice for the umber of process
    
    #Create the process & assisgn a function for ea ch process
    for i in range(num_processes):
        process=Process(target=square_numbers)
        processs.append(process)

    #start all process
    for process in processs:
        process.start()

    #wait for all process to finish
    # block the in process until these process are finished 
    for process in processs:
        process.join()

    print("Completed")
    print(os.cpu_count())