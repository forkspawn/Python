#Queue without size limit

class Queue:
    def __init__(self):
        self.items=[]
    
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False

    def enQueue(self,value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    def deQueue(self):
        if self.isEmpty():
            return "There is no element in Queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is no element in Queue"
        else:
            return self.items[0]

    def delete(self):
        self.items=None


customQueue=Queue()
print(customQueue.isEmpty())
for x in range(10):
    customQueue.enQueue(x)

print(customQueue)

#Queue with size limit

class Queue_size:
    def __init__(self,maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 ==self.start:
            return True
        elif self.start==0 and self.top +1== self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top==-1:
            return Ture
        else:
            return False
         
    def enQueue(self,value):
        if self.isFull():
            return "The Queue is Full"
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value
            return "The element is inserted at the end of Queue"

    def deQueue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]

    def delete(self):
        self.items=self.maxSize=[None]
        self.top=-1
        self.start=-1

customQueue=Queue_size(8)
for i in range(8):
    customQueue.enQueue(i)
print(customQueue)
for i in range(4):
    customQueue.deQueue()
print("After dequeuing",customQueue)

 
