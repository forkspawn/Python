#simples for of algorithm
'''
for i=0 to n:
    temp=top[i]
    top[i]=left[i]
    left[i]=bottom[i]
    bottom[i]=right[i]
    right[i]=temp
'''

import numpy as np

myArray=np.array([[1,2,3],[4,5,6,],[7,8,9]])
print(myArray)

def RotateMatrix(matrix):
    n=len(matrix)
    for layer in range(n//2):
        first=layer
        last=n-layer-1
        for i in range(first,last):
            #save to element
            top=matrix[layer][i]
            #save left element to left
            matrix[layer][i]=matrix[-i-1][layer] 
            #save bottom element to left
            matrix[-i-1][layer]=matrix[-layer-1][-i-1]
            #move right to bottom
            matrix[-layer-1][-i-1]=matrix[i][-layer-1]
            #move to the right
            matrix[i][-layer-1]=top
    return matrix 

print(RotateMatrix(myArray))

