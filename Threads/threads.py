import threading

t=threading.current_thread().getName()
if threading.current_thread()==threading.main_thread():
    for x in range(10):
        if x%2==0:
            print(x)
else:
    print("The running thread is not a Main Thread")    
print(t)

threading.current_thread().name="Burcu"
print(threading.current_thread().getName()) #MainThread


#Three ways created thread with python:
#-using the function
#-extending the thread class
#-without extending the thread class


#Using Functions to create Thread
#Fonksiyonun dışındaki her thread main thread olur.
from threading import Semaphore, Thread

def evenNumber():
    for x in range(20):
        if x%2 is 0:
            print(x)
     
    a=threading.current_thread().getName() 
    print(a)  #Thread-1

# a=threading.current_thread().getName() 
# print(a)  #MainThread          
# t=Thread(target=evenNumber)
# t.start()


#Targeting Multiple Thread
def even_odd():
    print("Even No are:")
    evenNo()
    #print(threading.current_thread().getName()) #Thread-1
    oddNo()
    
def evenNo():
    for x in range(10):
        if(x%2 is 0):
            print(x)
    print(threading.current_thread().getName()) #Even_Odd Thread
def oddNo():
    print("Odd No are:")
    for x in range(10):
        if(x%2 is not 0):
            print(x)
 
            

# t=Thread(target=even_odd,name="Even_Odd Thread") #Even_Odd Thread
# t.start()    

#Extending the thread class
class MyThread(Thread):
    def run(self):
        print("Egyptian Pyramid")
        print(threading.current_thread().getName()) #Thread-1
        for x in range(0,5):
            for j in range(0,x+1):
                print("*",end=" ")
            print("\r")


obj=MyThread()
obj.start()
#obj.run() #MainThread


#Without extending the thread class
class myThread:
    def naturalNo(self):
        if(threading.current_thread().getName()=="Thread-1"):
            for x in range(10):
                print(x)
        else:
            print("Hey this is not Thread-1")   
            
myobj=myThread()
t=Thread(target=myobj.naturalNo)
t.start()



#Multi-Threading
from time import sleep

def NaturalNo():
    
    print(threading.current_thread().getName(),"Has Started") #Thread-1
    sleep(2)
    for x in range(10):
        print(x)
        
    print(threading.current_thread().getName(),"Has Ended")  #Thread-2 

t1=Thread(target=NaturalNo)
t2=Thread(target=NaturalNo)
t1.start()        
t2.start()


#Programming the Scenario
class flightReservation:
    #l=Lock()
    l=Semaphore()
    def __init__(self,ticket_left):
        self.ticket_left=ticket_left
    l.acquire()    
    def buy(self,ticketRequested):
        if(self.ticket_left>=ticketRequested):
            print("Your Ticket is confirmed")
            print("Please make a Payment and take your ticket")
            self.ticket_left-=ticketRequested            
        else:
            print("There is not enough tickets Remaining")
    l.release()    
myobj =flightReservation(10)  
t1=Thread(target=myobj.buy,args=[3])
t2=Thread(target=myobj.buy,args=[4])
t3=Thread(target=myobj.buy,args=[3])
t1.start() 
t2.start()  
t3.start()            
