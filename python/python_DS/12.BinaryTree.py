#with LinkedList

import Queue as queue

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
    
def preOrderTraversal(rootNode):
     if not rootNode:
         return
     print(rootNode.data)
     preOrderTraversal(rootNode.leftChild)
     preOrderTraversal(rootNode.rightChild)

def PostorderTraversal(rootNode):
    if not rootNode:
        return
    PostorderTraversal(rootNode.leftChild)
    PostorderTraversal(rootNode.rightChild)
    print(rootNode.data)

def InorderTraversal(rootNode):
    if not rootNode:
        return
    InorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InorderTraversal(rootNode.rightChild)

'''
#made using queue LinkedList
def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enQueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.deQueue()
            print(root.value.data)
            if(root.value.leftChild is not None):
                customQueue.enQueue(root.value.leftChild)
            if(root.value.leftChild is not None):
                customQueue.enQueue(root.value.rightChild)    

def SearchBT(rootNode,nodeValue):
    if not rootNode:
        return "The BT does not exits"
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data==nodeValue:
                return "Success"
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.rightChild) 
                return "Not Found"

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        customQueue=queue.Queue()
        customQueue.dequeue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return "Successfully Inserted"

'''
 

newBT=TreeNode("Drinks")
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")

newBT.leftChild=leftChild
newBT.rightChild=rightChild

preOrderTraversal(newBT)

