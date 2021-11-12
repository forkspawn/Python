class computer:

    def __init__(self):
        self.name='koma'
        self.age=28
    
    def printval(self):
        print("name is",self.name,"age is", self.age)


c1=computer()
c1.name='Rashi'
c1.age=34

c2=computer()
print(c1.printval)
print(c2.name)
