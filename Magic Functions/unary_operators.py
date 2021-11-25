#Unary Operations 
# (-) --> __neg__(self,other) = Neg
# (+) --> __pos__(self,other) = Pos
# (abs) --> __abs__(self,other) = Abs
# (~) --> __invert__(self,other) = Invert
# (cmp) --> __complex__(self,other) = Complex
# (int) --> __int__(self,other) = Integer
# (long) --> __long__(self,other) = Long
# (float) --> __float__(self,other) = Float
# (oct) --> __oct__(self,other) = Octal
# (hex) --> __hex__(self,other) = Hexa

class x:
    def __init__(self,y):
        self.y=y
        
    def __neg__(self):
       return self.y
     
    def __pos__(self):
        return self.y 
     
    def __invert__(self):
        return self.y 
     
            
if __name__=="__main__":
    obj1=x(-2)
    print(-obj1)
    print(+obj1)
    print(~obj1)