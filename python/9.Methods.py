# three methods 
# 1. instance methods
# 2. class methods
# 3. static methods

class student:

    school = 'School' #class variables applies for every object

    def __init__(self,m1,m2,m3):
        self.m1=m1 #instance variables
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls): #this is class method, to not have an argument specified while calling we need to use a decorator
        return cls.school

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value

    @staticmethod
    def info_static():
        print("This is student class: which has nothing to do other methods")


s1=student(32,42,12)
s2=student(34,12,64)



print(s1.avg())
print(student.info())
print(s1.info())
