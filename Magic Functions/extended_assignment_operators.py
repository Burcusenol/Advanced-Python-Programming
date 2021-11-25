#Comparison Operations 
# (+=) --> __iadd__(self,other) =Add
# (-=) --> __isub__(self,other) =Sub
# (*=) --> __imul__(self,other) =Mul
# (/=) -->__idiv__(self,other) =Div
# (//=) -->__ifloardiv__(self,other) =Floor
# (%=) -->__imod__(self,other) =Mod
# (**=) -->__iow__(self,other) =Power
# (<<=) -->__ilshift__(self,other) =Left Shift
# (>>=) -->__irshift__(self,other) =Right Shift
# (&=) -->__iand__(self,other) =And
# (^=) -->__ixor__(self,other) =Xor
# (|=) -->__ior__(self,other) =Or


class eao:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
        
    def __iadd__(self,other):
        x=self.x + other.x
        y=self.y + other.y
        return eao(x,y)    
        
    def __isub__(self,other):
        x=self.x - other.x
        y=self.y - other.y  
        return eao(x,y)
    
obj1=eao(2,3)
obj1 -= eao(3,5)
print(obj1)    