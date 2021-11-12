
from functools import reduce #need this to use reduce

def update(n):
    return n*2

num=[2,1,23,4,1,23,12,1,445,46,4]

even=list(filter(lambda n: n%2==0,num)) #filter takes two arguments one fucntion and another one iterable, here rather than function we gave lambda and the iterable is a list, and we type casted it to list
print(even)

#map performs an operation to the data provided here we are performing bu multiplying it with 2

doubles=list(map(update,even )) #or we can use lambda  lambda n:n*2
print(doubles)

#reduce 

sum=reduce(lambda a,b: a+b ,doubles) # this adds all the values in the double list
print(sum)
