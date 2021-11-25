#Features of MetaProgramming
#-Decorators
#-Class Decorators
#-Meta Classes

#Types of Decorators:
#-Function Decorators
#Class Decorators

#Function Decorators

def outside_function():
    def inside_function():
        print("Hey I am the inside function")
        #outside_function() #errors
        
    print("Hey I am the outside the function")
    print("Above we are the statements that are executed before inside function")
    inside_function()
    print("Below we are the statements that are printed after the inside function")
    
outside_function()
#***************************#
def addition(a,b):
    def add(x,y):
        return x+y
    sum="The sum of two numbers is " + str(add(a,b))
    return sum

answer=addition(2,3)
print(answer)
#****************************#
def x(func):
    print("I am the function x")
    
def y():    
    print("Hi I am the function y")
    
    
x(y())    

#*****************************#
def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function

z=outer_function(2)
v=outer_function(3)

ans1=z(4)
ans2=v(5)
print(ans1)
print(ans2)
#******************************#
def poly(a,b,c):
    def pol(x):
        return a*x**2 + b*x + c
    return pol

ans1=poly(1,2,3)
ans2=poly(5,6,7)
v=ans2(8)
z=ans1(4)
print(z)
print(v)

#Features:
#-function inside function
#-function as argument
#-return function

def outer_function(a):
    def inner_function(b):
        return a+b
    return inner_function

def repatable(b):
    x=outer_function("Hello ")
    d=x(b)
    print(d)
    
    
repatable("Burcu")
repatable("Ali")
#**************************#
def join(function):
    function.data=2
    return function

def add(x,y):
    return x+y+add.data

join(add)
c=add(5,4)
print(c)
#**************************#
def x(a):
    validate_a="hello "
    if a is not validate_a:
        #a=validate_a
        print("not a valid input")
    
    def y(b):
        validate_b="ali"
        if b is not validate_b:
            #b=validate_b
            print("not a valid name")
        return a+b
    return y

def repeatable(a,b):
    c=x(a)
    d=c(b)
    print(d)
    
repeatable("hi ","burcu")
#******************************#
def argument(f):
    def helper(x):
        if type(x)==int and x>0:
            return f(x)
        else:
            raise Exception("Argument is not a positive integer value")
        
def factorial(n):
    if n==1:
        return 1 
    else:
        return n * factorial(n-1)
    
z=factorial(5)
print(z)       
        