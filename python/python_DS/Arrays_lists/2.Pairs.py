# write a program to find all pairs of integers whose sum equal to a given number

def pairsofIntegers(number):
    if (number%2)==0:
        count=0
        while(number!=0):
            number=int(number//2)
            count=count+1
        return count+1
    else:
        count =0 #missing logic in odd part, here we took int(numerator//denominator) cause this mimicks 'C' division
        while(number!=1):
            number=int(number//2)
            count=count+1
        return count+1

#print(pairsofIntegers(int(input('Enter the number'))))

myList=[1,2,3,4,5,6,7,8,9,10]
print(myList)

def takepairs(number):
    place=number
    if(number==place/2):
        return
    number=number/2
    return print(takepairs(number),takepairs(number-1))

#takepairs(10)

#real solution

def findPairs(list,sum): #not for same repeating elements like 5,5 for 10, if you want that put only 'i' in range of j, as that will compare value with itslef
    for i in range(len(list)):
        for j in range(i+1,len(list)): #from second element onwards
            if (list[i]+list[j]) == sum:
                print(list[i],list[j])

findPairs(myList,int(input('Enter the value till the list')))
        
