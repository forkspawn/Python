class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name, self.rollno)

    class laptop:

        def __init__(self):
            self.brand='dell'
            self.cpu = 'i5'
            self.ram= 8


s1=student('offff',2)
s2=student('kuuuuf',3)

print(s1.name, s1.rollno)

s1.show()

lap1=s1.lap
lap2=s2.lap
