class x:
    def __init__(self) :
        print("An instance or object was initialised")
        
    def __call__(self, *args, **kwargs):
        print("Arguments are",args,kwargs)
        
        
a=x()
print("Calling objects or arguments")
a(4,5,z=12,v=20)
print("calling call function again")
a(8,9,r=30,t=40)

#**************************#
def x():
    print("doing something using function decorators")
    def y():
        print("naming "+x.__name__)
    return y


def repetable():
    c=x()
    d=c()
    

repetable()    
#*************************#
class x:
    def __init__(self) :
        print("doing something using class decorator")
        
    def __call__(self) :
        print("naming " + x.__name__)
        

def repetable():
    c=x()
    c()        
    
    
repetable()