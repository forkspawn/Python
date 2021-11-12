#polymorphism
# duck typing
# operator overloading
# method overloading
# method overriding

# duck typing

x=5
x='oofff'

class pycharm:

    def execute(self):
        print("compiling " + "running")

class myeditor:

    def execute(self):
        print("selfcheck ")
        print("compiling "+ "running")

class laptop:

    def code(self,ide):
        ide.execute()

ide=pycharm() #here we have created an object of pycharm which has a method execute
#ide = myeditor if we changed this the code stil works cause it also has a method called execute

lap1=laptop()
lap1.code(ide)

#operator overloading

a=5
b=6

print(a+b)
print(int.__add__(a,b))

class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1 + other.m1
        m2=self.m1 + other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self,other):
        r1=self.m1 + self.m2
        r2=other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False
    
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1 = student(58,69)
s2 = student(32,12)

s3 = s1 + s2 #as both s1 and s2 are student class, and __add__ method is '+', so if we use '+' __init__ method is called
print(s3.m1)

if s1>s2:
    print("s1 is big")
else:
    pritn("s2 is big")

# return '{} {}'.format(self.m1, self.m2) can be used this to print in return

#method overloading
#not in python
# method overloading is having same method names with different arguments in the same class
# class :
# def ave(a,b): 
# def ave(a,b,c): 
# when you have to pass lesser arguments you can put def sum(a=none,b=none,c=none)
# if a!=None and so on for each cases
    # then s=a+b+c

#method overriding

class A:
    def show(self):
        print("in a show")

class B(A):
    def show(self):
        print("in B show")


a1=B()
a1.show()
 
