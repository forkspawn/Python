class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:  
                break
        node=node.next

    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "The CSLL has been created"
    
    def insertCSLL(self,value,location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode=Node(value)
            if location == 0: #at the begining
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1: #at the end
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=newNode
            return "The Node has been succesfully created"
    
    def TraversalCSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    break

    def SearchCSLL(self,nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value== nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    return "The node does not exist in this CSLL"
    
    def DeleteCSLL(self,location):
        if self.head is None:
            print("There is not any node in CSLL")
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location == 1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node = node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
    
    def deleteEntireCSLL(self):
        self.head=None
        self.tail.next=None
        self.tail=None




list1=CircularLinkedList()
list1.createCSLL(1)
list1.insertCSLL(0,0)
list1.insertCSLL(4,0)
list1.insertCSLL(5,0)
list1.insertCSLL(6,0)
list1.insertCSLL(9,0)
list1.TraversalCSLL()
list1.DeleteCSLL(0)

print([node.value for node in list1])
