#given two strings, if the other string is an permutation of the other

def StringPermutation(string1,string2):
    lis1=string1
    lis2=string2
    temp=""
    print(lis1)
    print(lis2)
    
    if len(lis1)!=len(lis2):
        return "Not a permutation"

    for i in lis1:
        if i in lis2:
            temp=temp+i
           # print(temp)
        if len(temp)==len(lis1):
            print(temp)
            return  "its a permutation"
        if lis1[3] not in temp:
            print(temp)
            return "its not a permutation"

#print(StringPermutation(str(input('Enter a string \n')),str(input('Enter another string \n'))))

#given solution

def permutation(list1,list2):
    list2.reverse()
    if list1==list2:
        return True
    else:
        return False

print(permutation([1,2,3],[3,2,1]))
