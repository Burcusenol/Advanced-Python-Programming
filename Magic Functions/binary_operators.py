#Binary Operations 
# (+) --> __add__(self,other) = Add
# (-) --> __sub__(self,other) = Sub
# (*) --> __mul__(self,other) = Mul
# (/) --> __div__(self,other) = Div
# (//) --> __flooardiv__(self,other) = Floor
# (%) --> __mod__(self,other) = Mod
# (**) --> __pow__(self,other) = Power
# (<<) --> __lshift__(self,other) = Left Shift
# (>>) --> __rshift__(self,other) = Right Shift
# (&) --> __and__(self,other) = And
# (+) --> __add__(self,other) = Add
# (-) --> __sub__(self,other) = Sub
# (*) --> __mul__(self,other) = Mul
# (/) --> __div__(self,other) = Div
# (//) --> __flooardiv__(self,other) = Floor
# (+) --> __add__(self,other) = Add
# (-) --> __sub__(self,other) = Sub
# (*) --> __mul__(self,other) = Mul
# (^) --> __xor__(self,other) = Xor
# (|) --> __or__(self,other) = Or


class Addition:
    def __init__(self,*arguments):
        if len(arguments) == 0:
            self.numbers=(0,0)
        else:
            self.numbers=arguments
            
    
    def __add__(self,other):
        sum=tuple(x+y for x,y in zip(self.numbers,other.numbers))  
        return Addition(*sum)   
        #(1,5)
        #(2,3)
        #(4,5)
        #(8,1)
        #Output:(15,14)   

    def __mul__(self,other):
        mul=tuple(x* y for x,y in zip(self.numbers,other.numbers))
        return Addition(*mul)

    def  __sub__(self,other):
        sub=tuple(x-y for x,y in zip(self.numbers,other.numbers))
        return Addition(*sub)


obj1=Addition(2,3)
obj2=Addition(4,5)
obj3=Addition(3,5)
obj4=obj1+obj2+obj3
obj5=obj1 * obj2 * obj3
obj6=Addition(3,4)
obj7=Addition(1,2)
obj8=obj6-obj7
obj9=obj1 + (obj2 * obj3)
print("Sum : ",obj4.numbers)
print("Mul : ",obj5.numbers)
print("Sub : ",obj8.numbers)
print("Sub+Mul : ",obj9.numbers)