import numpy as np

myArray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])


def maxproduct(array):
    lis1=list(array) #converting array into a list
    max1=max(lis1)   #finding the max elemenet in the list
    lis1.remove(max1) #remving the max element so that we can find the next max elemet
    max2=max(lis1)   #second max element
    return max1*max2 #returning the max of two

print(maxproduct(myArray))

#given solution

def FindMaxProduct(array):
    maxproduct=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j]>maxproduct:
                maxproduct=array[i]*array[j]
    return maxproduct

print(FindMaxProduct(myArray))
