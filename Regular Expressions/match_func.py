#match(pattern,sequence,flags)
import re

pattern=r"Burcu"
sequence="Burcu"
if re.match(pattern,sequence):
    print("Match Found")
else:
    print("Match not found")


#**********************************#

sequence="Burcu Senol make tutorials"
x=re.match(r'(Burcu) (Senol)',sequence)

if x:
    print(x.group()) #burcu
    print(x.group(0)) #burcu
    print(x.group(1)) #error because only one item Burcu
    print(x.group(2)) #Senol
    print(x.group(1,2)) #('Burcu', 'Senol')
    
    
#***********************************#

sequence="udemy@gmail.com"
x=re.match(r'(udemy)(@)(gmail.com)',sequence)
if x:
    print(x.group())    #udemy@gmail.com
    print(x.group(1)) #udemy
    print(x.group(1,2,3)) #('udemy', '@', 'gmail.com')
    
#************************************#

#Specific Characters 

#. new line
#\w -->any single character
#\W -->single letter mathces upper
#\s --> like space tab
#\S 
#\t
#\n -->match new line
#\r --> redone
#\d --> decima from zero to one
#^ -->start string
#$ 
#[abc]
#[a-zA-Z0-9]
#(0-9)
#\A    
#\b
#\
#+
# '*'
# '?'
# '*? +? ??'
#{x}
#{x,y}
#{x.y}?
#[]    


x=re.search(r'Burcu\\sSenol','Burcu\sSenol').group()
print(x)  #Burcu\sSenol

y=re.search(r'Burcu\sSenol','Burcu Senol').group()
print(y) # Burcu Senol

#***************************************#

x=re.search('(?<=abc)xyz' ,'abcxyz')
print(x.group(0))  #xyz


y=re.match(r'(?<=abc)xyz' ,'abcxyz')
print(y.group(0))  #error

#**************************************#
x=re.search(r'\d{9.10}','0987654321').group()
print(x) #0987654321

#re.I -->ıgnorecase 

    
    
