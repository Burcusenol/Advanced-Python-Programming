def x(sentence,next_coroutine):
    y=sentence.split(" ")
    for z in y:
        next_coroutine.send(z)
    next_coroutine.close()
    
    
def u(pattern="Burcu",next_coroutine=None):
    print("searching string{}".format(pattern))
    try:
        while True:
            z=(yield)
            if pattern in z:
                next_coroutine.send(z)
                
    except GeneratorExit:
        print("Done with the matching process")
        
        
def printing():
    try:
        while True:
            z=(yield)
            print(z)
    except GeneratorExit:
        print("Done pipelining")            


d=printing()
d.__next__()
f=u(next_coroutine=d)
f.__next__()



sentence="My name is Burcu and ı make tutorials"

x(sentence,f)