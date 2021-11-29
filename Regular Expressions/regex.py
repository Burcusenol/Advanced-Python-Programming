import re
TabError
test_string='123abc456789abc123ABC'

pattern=re.compile(r'abc')
matches=pattern.finditer(test_string)

for match in matches:
    print(match)  #<re.Match object; span=(3, 6), match='abc'>
                    #<re.Match object; span=(12, 15), match='abc'>
                    
                    
#matches=re.finditer(r'abc',test_string)
#************************#
a="\tHello"
print(a) #  Hello -->bir tab boşlukla yazar

a=r"\tHello" #\tHello -->hepsini bir dize olarak ele alır
print(a)

#match() , search() ,findall()

#FİNDALL()
pattern=re.compile(r'abc')
matches=pattern.findall(test_string)

for match in matches:
    print(match) # abc abc


#***************************#
#MATCH()  --> return only one match 
    
pattern=re.compile(r'abc')  #(r'123) -->print =#<re.Match object; span=(0,3), match='123'>
match=pattern.match(test_string)

print(match) # None

 #***************************#   
#SEARCH()
    
pattern=re.compile(r'abc')  #(r'123) -->print =#<re.Match object; span=(0,3), match='123'>
match=pattern.search(test_string)

print(match)  #<re.Match object; span=(3, 6), match='abc'>

#***************************#
pattern=re.compile(r'abc')
matches=pattern.finditer(test_string)

for match in matches:
    print(match.span(),match.start(),match.end()) #(3, 6) 3 6 (12, 15) 12 15
    print(match.group()) #abc abc
    
#***************************#   
    
pattern=re.compile(r'.')
matches=pattern.finditer(test_string)

for match in matches:
    print(match.group()) ## all characters
    
    
#***************************#

pattern=re.compile(r'^123') #-->başlangıçtan arar
matches=pattern.finditer(test_string)

for match in matches:
    print(match.group()) # 123 
    
    
#123$ --> sonda arama yapar
#****************************#

test_string="hello 123_ heyho hohey"

pattern=re.compile(r'\d') #-->başlangıçtan arar
matches=pattern.finditer(test_string)

for match in matches:
    print(match)  # sayılar bulur



#\D -->tüm karakterleri bulur 
#\s --> boşluk bulur
#\W --> boşlukları bulur
#[lo] --> parantez içindeki karakterleri arar
   
   
test_string='hello world, you are the best world'
pattern=re.compile(r'world')
subbed_string=pattern.sub("planet",test_string)
print(subbed_string) # hello planet,you are the best planet   


   
   