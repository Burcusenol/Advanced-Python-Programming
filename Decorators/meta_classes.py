class x:
    pass

x.variable=10

c=x()

print(c.variable)
#**********************#
def metafunc():
    print("I am the meta class function")


class inherit:
    def func(self):
        print("I am the inherited method")

metaobject=type('meta',(inherit,),dict(name="Burcu",metafunction=metafunc))

print(type(metaobject))

b=metaobject()

print(type(b))

b.func()
print(b.name)