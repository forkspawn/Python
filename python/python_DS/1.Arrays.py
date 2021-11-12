from array import*
#syntax: arrayName=array(typecode,[initializer])
print("Creating an array and inserting 7 and 99 ")

arr1=array('i',[1,2,3,4,5])
print(arr1)

arr1.insert(6,7) #def insert(i: int,x: _T), i is the position 
print(arr1)

arr1.insert(0,99) #inserting at first, this shifts the remaining elements to the right
print(arr1)

#1.array traversal
print("Array traveral")
def traversalArray(array):
    for i in array:
        print(i)

traversalArray(arr1)
print("\n")


#2.access array element
print("Accessing array elements ")

def accessElement(array,index):
    if index>len(array):
        print("There is not any element in the index")
    else:
        print(array[index])

accessElement(arr1,0)
print("\n")

#3.finding an element
print("Finding an element in an array ")

def searchArray(array,value):
    for i in array:
        if i==value:
            return array.index(value) #index function returns index
    return "The element doesn't exits"

print("The element is at index")
print(searchArray(arr1,4))
print("\n")

#4.deleting an element
print("Deleting an element at the position")

arr1.remove(1) #1 is the position of the index and it shifts the values to the empty postion
print(arr1)
print("\n")

#5.append method
# adds an element to the end of an array
print("Append method to add element at the last ")

arr1.append(6)
print(arr1)
print("\n")

#6.extend python array using extend method
print("Extend method to extend the array with another array ")

myar1=array('i',[12,43,12])

myar1.extend(arr1)
print(myar1)
print("\n")
#7.add items from list into array using fromlist() method
print("To add elements to the array from the list ")

templist=[1,23,13,43,54,12,43,2]
myar1.fromlist(templist)
print(myar1)
print("\n")

#8.remove any array element using remove
print("Remove an array element ")

myar1.remove(23)
print(myar1)
print("\n")

#9.pop method to remvoe last element of the array
print("pop method to remove the last element in an array ")

myar1.pop()
print(myar1)
print("\n")

#10.fetch any element throught its index using index() method
print("index method to get element at the particular index ")

print(myar1.index(12))
print("\n")

#11.reverse a python array using reverse() method
print("reverse a array using reverse method ")

myar1.reverse()
print(myar1)
print("\n")

#12.get array buffer information through buffer_inf() method
print("This is the array buffer information in the memory")
print(myar1.buffer_info())
print("\n")

#13.check for number of occurences of an element using count() method
print("The count method")
print(myar1.count(12))
print("\n")

#14.convert array to string using tostring() method
print("Converting an array into a string")
strtemp=myar1.tostring()
print(strtemp)
ints=array('i')
ints.fromstring(strtemp)
print(ints)

#15. convert array to a python list with same element using tolist()method
print("converting an array to a list")
print(arr1.tolist())

#16.append a string to char array using fromstring() method
print("appending an string to an char array")
#go to 14

#slicing elements from an array
print("slicing an element from the array")
print(arr1[1:6])























