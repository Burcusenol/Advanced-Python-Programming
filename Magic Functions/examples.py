class dictionary(dict):
    def __add__(self,other):
        self.update(other)
        return dictionary(self)
    
    
dict1=dictionary({'firstname':'Burcu'})
dict2=dictionary({'lastname' :'Senol'})    
print(dict1 + dict2)


class comp:
    def __init__(self,x):
        self.x=x
        
    def __lt__(self,other):
        return self.x < other.x    
    
    def __gt__(self,other):
        return self.x > other.x  
    
    def __eq__(self,other):
        return self.x == other.x   
    
    
    
if __name__=="__main__":
    x=comp(2)
    y=comp(5)
    print(x>y)
    print(x<y)
    print(x==y)    
    
    
class Length_Conversion:   
    value={"mm":0.001,"cm":0.01,"m":1,"km":1000,"in":0.0254,
       "ft":0.3048,"yd":0.9144,"mi":1609.344} 

    def __init__(self,x,value_unit="m"):
        self.x=x
        self.value_unit=value_unit
     
    def convert_to_metres(self):
        return self.x*Length_Conversion.value[self.value_unit] 
        
    def __add__(self,other):
        ans=self.convert_to_metres() + other.convert_to_metres()
        return Length_Conversion(ans/Length_Conversion.value[self.value_unit],self.value_unit)
    
    def __str__(self):
        return str(self.convert_to_metres)
    
    def __repr__(self):
        return "Length_Conversion(" + str(self.x) + ", " + self.value_unit + ")"
       
       
if __name__=="__main__":    
    obj1=Length_Conversion(5.5, "yd") + Length_Conversion(1)
    print(repr(obj1)) 
    print(obj1)  