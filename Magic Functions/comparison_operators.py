#Comparison Operations 
# (<) --> Obj__It__(self,other)
# (>) --> Obj__gt__(self,other) 
# (==) --> Obj__eq__(self,other) 
# (>=) -->Obj__ge__(self,other) 
# (<=) -->Obj__le__(self,other)
# (!=) -->Obj__ne__(self,other)

class comparison:
    def __init__(self,x):
        self.x=x
        
        
    def __lt__(self,other):
        return self.x < other.x
    
    def __gt__(self,other):
        return self.x > other.x
    
    def __eq__(self,other):
        return self.x == other.x
    
        
if __name__=="__main__":
    obj1=comparison(6)
    obj2=comparison(4)  
    print(obj1 < obj2)
    print(obj1 > obj2)
    print(obj1 == obj2)
          