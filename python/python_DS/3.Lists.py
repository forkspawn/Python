#lists
#1. ordered collection of items
#2. can have different data types

#traversing thourgh lists

shoppinglist=['milk',23,12,'cheess',2,1,4,'copernicus']

for i in range(len(shoppinglist)):
    print(shoppinglist[i])

for i in shoppinglist:
    print(i)

#update/isnert in a list
shoppinglist[2]='updated'
print(shoppinglist)

#concatenates adds two lists
a = [3,23,5,3]
b = [2,5,4,64,0]
c = a+b
print(c)

# *operator

a=[2]
a=a*4
print(a)

#max
print(max(a))

#calculate the average from user input
'''
total=6
count=0
while(True):
    inp=input('Enter a number')
    if inp=='done':break
    value=float(inp)
    total=total+value
    count=count+1
    average=total/count
print('Average',average)
'''

#strings ans lists

a='spam'
b=list(a)
print(b)
ele=[3,12,345,25,42,34,56,43]
b='spam-spam-spam'
delimiter='-'
c=b.split(delimiter)
print(c)
print(delimiter.join(b))
s=ele.sort()
s=ele
print(s)
