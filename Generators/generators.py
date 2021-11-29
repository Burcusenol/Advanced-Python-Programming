x=[1,2,3,4,5]
import time
def call_received(recieved):
    a=0
    while True:
        if recieved=='yes':
            a=a+1
            return a
        else:
            return a
    
stoppage_time=time.time()+5*60

while time.time()<stoppage_time:
    recieved=input("did you received a call or not : ")
    total=call_received(recieved)
    print(total) #1-1-1-1-1
                     
#**********************************#

def x():
    yield 'a'
    yield 'b'
    yield 'c'

y=x()
for i in range(3):
    print(y.__next__())  # a-b-c

#***********************************#
import time
def calls_recieved(recieved=None):
    a=0
    while True:
        if recieved=='yes':
            a=a+1
            recieved=yield a
        else:
            recieved=yield a
            
    
    
rec=calls_recieved()
rec.__next__()
         
  
stoppage_time=time.time()+5*60
while time.time()<stoppage_time:
    ans=input("did you received a call or not : ")
    print(str(rec.send(ans))) #1-2-3-4-5