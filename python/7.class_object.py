class computer:
   
    def __init__(self,cpu,ram): #gets called automatically
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("something that computer has",self.cpu,self.ram)

comp1=computer('rizen',32) 
#crearting an object of computer and naming as comp1

print(type(comp1)) #this prints the type of the object

comp2=computer('i5',16) 

#computer.config()
#computer.config(comp2)

comp1.config()
comp2.config()


