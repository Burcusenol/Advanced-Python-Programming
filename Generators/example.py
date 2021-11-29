def reverse(str):
    length=len(str)
    for i in range(length,-1,-1,-1):
        yield str[i]
        
for char in reverse ("Burcu"):
    print(char)
    
    
#Python genrator expression 
# # y=([expression])
y=[1,2,3,4,5]
print([x**2 for x in y])  #[1,4,9,16,25]

print((x**2 for x in y).__next__()) #[1,4,9,16,25]

class power:
    def __init__(self,max=0):
        self=max=max
        
    def __iter__(self,n):
        self.n=n        
        return self
    
    def __next__(self): 
        if self.n>self.max:
            raise StopIteration
        result=2**self.n
        self.n+1
        return result
    
x=power(5)
x.__iter__(2)
print(x.__next__())

#**************************#
def gen(max=0):
    a=2
    while a<max:
        yield 2 **a
        a+=1
        
        
print(gen(5).__next__())