#Get,set and Del Descriptors
#get(self,instance,owner)
#set(self,instance,value)
#delete(self,instance)



class cel:
    def __get__(self,instance,owner):
        return 5*(instance.x-32)/9
    
    def __set__(self,instance,value):
        instance.x=32+9*value/5
        
class Temp:
    y=cel()
    def __init__(self,x):
        self.x=x
 
        
t=Temp(112)       
print(t.y)
t.y=0
print(t.x)

#***************************************#
class cel:
    def __init__(self,value=0.0):
        self.value=value
    
    def _get__(self,instace,owner):
        return self.value
    
    def __set__(self,instance,value):
        self.value=float(value)    



class feh:
    def __get__(self,instance,owner):
        return instance.cel * 9 / 5 + 32
    
    def __set__(self,instance,value):
        instance.cel=(float(value)-32)*5/9
        

class temp:
    cel=cel(112)
    feh=feh()   
    print("*******")  
    print(cel.value)   
    