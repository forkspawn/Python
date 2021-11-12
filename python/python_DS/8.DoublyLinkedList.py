class Node:
    def __init__(self,value=None):
        self.data=value
        self.prev=None
        self.next=None

class DoublyLinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None

    def CreateDLL(self,value):
        node=Node()
        node.data=value
        self.head=node
        self.tail=node
        return "Node has been created"

    def InsertDLL(self,value,position):
        node=Node()
        node.data=value

        if(position=='Begin' or 0):  #insert at beginning
            self.head.prev=node
            node.next=self.head
            node.prev=None
            self.head=node

        elif(position=='Last'):
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
            node.tail=None

        else:
            index=0
            trav=self.head
            for i in range(position):
                trav=trav.next

            node.next=trav
            node.prev=trav.prev
            trav.prev.next=node
            trav.prev=node



    def TraversalDLL(self):
        trav=self.head
        while trav is not None:
            print(trav.data)
            trav=trav.next

       
list1=DoublyLinkedList()
list1.CreateDLL(1)
list1.InsertDLL(0,'Begin')
list1.InsertDLL(2,1)
list1.InsertDLL(3,2)
list1.InsertDLL(4,3)
#list1.InsertDLL(5,'Last')
list1.InsertDLL(23,4)
list1.InsertDLL(24,5)
list1.InsertDLL(22,4)
list1.TraversalDLL()

