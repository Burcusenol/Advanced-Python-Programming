# re.compile(pattern,flag)
# re.seaarch(pattern,string,flag)
# re.match(pattern,string,flag)
# re.split(pattern,string,max,flag)
# re.findall(pattern,string,flag)
# re.finditer(pattern,string,flag)
# re.sub(pattern,repl,flag)
# re.subn(pattern,repl,flag)
# re.sub(pattern)
import re

pattern="Burcu make tutorials"
x=re.compile(pattern)
y=x.match('Burcu make tutorials')
if y:
    print("Match found")
else:
    print("Match not found")
    
    
#********************************#

pattern="Burcu make tutorials"
x=re.match(pattern,"Burcu make tutorials")
if x:
    print("Match found")
else:
    print("Match not found")
    
    
#*********************************#

x=re.split('\W+','burcu,senol,udemy')
print(x)  #['burcu', 'senol', 'udemy']

y=re.split('(\W+)','burcu,senol,udemy')
print(y) #['burcu', ',', 'senol', ',', 'udemy']

#*********************************#

x=re.findall(r'Burcu Senol are','Burcu Senol Udemy')
print(x) #[]

#*********************************#

x=re.finditer(r'Burcu Senol are','Burcu Senol Udemy')
print(x) #<callable_iterator object at 0x0000023F742169D0>

#*********************************#

x=re.subn(r'Burcu Senol is ','Udemy','Burcu Senol',count=0)
print(x) #Udemy Tutorials =sub //subn (Burcu Senol,0)

#*********************************#
import string

pattern=string.ascii_lowercase
x=re.escape(pattern)
print(x)  #abcdefghijklmnopqrstuvwxyz

pattern=string.digits
y=re.escape(pattern)
print(y) # 0123456789

pattern="+-*&$#@"
z=re.escape(pattern)
print(z) #\+\-\*\&\$\#@

#********************************#

pattern=r'Burcu Senol Udemy'

x=re.match(pattern,'Burcu senol is')
if x:
    print("Cool")
else:
    re.error("Not Cool")