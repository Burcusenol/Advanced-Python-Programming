def searching(string):
    print("Searching String:{}".format(string))
    try:
        while True:
            name=(yield)
            if string in name:
                print(name)
    except GeneratorExit:
       print("Closing the CoRoutine")
              

x=searching("Burcu")
x.__next__()            

x.send("Burcu")
x.send("hello")
x.close()
x.send("Send some data")  #error