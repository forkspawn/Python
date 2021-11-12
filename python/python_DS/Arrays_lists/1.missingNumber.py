# how to find the missing number in an integer array of 1 to 100
#which contain interger between 1 and 10

def total(number,array): #number is the number of elements in the array
    sumof=0
    n=number*(number+1)/2
    for i in array:         #here we can use sum(array) to find the sum
        sumof=i+sumof
    return n-sumof

ar=[1,2,3,4,5,6,7,9,10]

print(total(10,ar))
