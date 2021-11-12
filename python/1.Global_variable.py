a=10
b=99
print(id(a)) #prints address of a

def something():
    a=9
    x=globals() #prints all the global variables ! research
    y=globals()['a']
    print(id(y)) #this has the same adress of
    print("in fun",a)
    globals()['a']=15 #this assigns value to a in the global variable but doesnt change in the local variable
    print("changed value of", a)

something()
print("outside ",a)

