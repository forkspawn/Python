class A:
   
    def __init__(self): 
        print("in a init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A): # with the brackets B is the child of A
    
    def __init__(self):
        super().__init__()
        print("init in b")

    def feature3(self):
        print("feature 3 is working")


class C(A,B):

    def __init__(self):
        super().__init__()
        print("in c init")

a1=A()

a1.feature1()

#constructor 
# it can be an init method

a2=B() #here we are assigning a2 object when we execute this we will be calling constructor of A, the init method
# if B has its own constuctor then it only calls init in B and doesnt call init in A

#if we want to call init method in A then we have to use 'super' keyword

a3=C()
#we are calling C class, as C is child of both A and B, if we use super to print the parent class it prints A, it is biased
# the order of priority is left to right

