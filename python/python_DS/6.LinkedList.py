class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def insert2SL(self,value,location):
        newNode=Node(value)
        
        if self.head is None:
            self.head= newNode
            self.tail= newNode
        else:
            if location == 0: #at the begining
                newNode.next=self.head
                self.head=newNode
            elif location ==1: #at the end
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
    
    def traversalSLL(self):
        if self.head is None:
            print("Singled Linked List does not exit")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
    
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue:
                    return node.value
                node=node.next
            return "The value doesnt exist"
    
    def deleteNode(self,location):
        if self.head is None:
            print("The single linked list does not exist")
        else:
            if location==0:

                 if self.head==self.tail:
                     self.head=None
                     self.tail=None
                 else:
                     self.head=self.head.next
            elif location ==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next




firstList=LinkedList()

firstList.insert2SL(1,1)
firstList.insert2SL(2,1)
firstList.insert2SL(3,1)
firstList.insert2SL(4,1)
firstList.insert2SL(99,3)
firstList.insert2SL(100,0)
print([node.value for node in firstList])

#firstList.traversalSLL()
#print(firstList.searchSLL(99))
firstList.deleteNode(0)
print(firstList.traversalSLL())
'''
SinglyLinkedList=LinkedList()
node1=Node(1)
node2=Node(2)

SinglyLinkedList.head=node1 #this assings node1 to head
SinglyLinkedList.head.next=node2 #this assigns next in node1 to node2
SinglyLinkedList.tail=node2 #this assins the tail of the node
'''


