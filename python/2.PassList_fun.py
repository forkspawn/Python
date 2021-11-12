
def count(lis):
    even =0
    odd=0
    for i in lis:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd 

lis = [23,1231,4,2,3,52,5,2,6,2,77,]

even,odd=count(lis)
print("even = {} and odd = {}".format(even,odd) ) # even and odd are reaplced with curly braces
