import numpy as np

# 1 - 2,12,4,2
# 2 - 23,12,53,1
# 3 - 2,12,4,1
# 4 - 65,3,2,1

twoDarray=np.array(([2,12,4,2],[23,12,53,1],[2,12,4,1],[65,3,2,1]))
print(twoDarray)

#Accessing an element in two dimensional array
def accessElemenets(array,rowIndex,colIndex):
    if rowIndex >=len(array) and colIndex >=len(array[0]):
        print("Incorrect Index")
    else:
       print( array[rowIndex][colIndex])

accessElemenets(twoDarray,1,2)
print(twoDarray[1][2])

#traversing two dimensional array
def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseArray(twoDarray)

#searchin an element in an array
def searchArray(array,value):
    for i in range(len(array)): #for rows
        for j in range(len(array[0])): #for column
            if array[i][j]==value:
                return 'The value is located at'+str(i)+" "+str(j)
    return 'The element not found'

print(searchArray(twoDarray,2))


#deletion an column or a row
newtwoDarray=np.delete(twoDarray,0,axis=0) #axis = 0 deletes first row
print(newtwoDarray)



