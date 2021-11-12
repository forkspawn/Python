
myList=[1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]

def UniqueElements(lists):
    count=[]
    value=0
    for i in lists:
        value=lists.count(i)
        if value>1:
            print(i, 'is not unique ')
        if value==1:
            print(i, 'is unique ')

UniqueElements(myList)

#given solution

def isUnique(lists):
    a=[]
    for i in lists:
        if i in a:
            print(i)
            return false
        else:
            a.append(i)
    return True

