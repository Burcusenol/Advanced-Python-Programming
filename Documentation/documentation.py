#DocStrings
class x:
    def __init__(self,y):
        self.y=y
        
    x=4
    k=10.0
    l=19.98
    
    def g(self):
        print("Hey I am the g function")
        
        
    def h(self):
        t=10
        print("hey I am the h function")
         
     
#help(x)   
#print(dir(x))         
#w=x(3)
#print(dir(x.k)) 
#print(dir(x.x))
#print(dir(w.x))   

#print(dir(x))
y="burcu"
#print(y.__doc__)

#***************************#
def x(name):
    print(name)
    
x.__doc__="Burcu"
print(x.__doc__)   #Burcu
print(x("Burcu"))  #None


#***************************#
#DocStrings Type
#-pakage docString
#-class docStrig
#-sript docString


#**************************#
#Comments

a=4 #It is a variable whose value equals to 4
#Step-1
#This is an additon funcion
def add(a,b):
    print(a+b)
    
    
def sub(a,b):
    print(a-b)
    
def mul(a,b):
    print(a**b)        


