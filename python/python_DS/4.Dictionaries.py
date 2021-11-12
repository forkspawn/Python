#dictionary is a collectio which is unordered, changeable and indexed

EngtoSp={'one':'uno','two':'dos','three':'tres','word':'meanning'}
print(EngtoSp)

#traversing through a dictionary
def traverseDict(dict):
    for key in dict:
        print(key,dict[key])

traverseDict(EngtoSp)

#searching a element
def searchDict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return 'The value does not exist'

#delete an element in dictionary
#myDict.popitem() remove the last element in the dictionary
# del myDict{'age'}

#clear method deletes everything
#myDict.clear() it doesnt take any arguments

#copy method
anotherDict=EngtoSp.copy()
print(anotherDict)

#fromkeys() method creates an new dictionary from the keys where the value can be same
keysdict={}.fromkeys([1,2,3,4,5,],0)
print(keysdict)

#get() returns 1 if found or returns none
#syntax: dictionary.get(key,value)
print(EngtoSp.get('one',0))
#if one is found it returns the value or else zero,that we have mentioned

#items()
#syntax: dictionary.items() it doesnt take any parameter

#keys()
#gives the list of all keys in the dictionary
#syntax: dictionary.keys()
print(EngtoSp.keys())

#setdefault()
# returns the valuue of the key it its present in the dictionary
#syntax: dictionary.setdefault(key,default_value)

#values()
#returns values in the dictionary 
#syntax: dictionary.values()

#update()
#syntax: dictionary.update(other_dictionary)

#all method
#all(dictionary) if all elements are true return true

#sorted()
#sytanx: sorted(EngtoSp,key=len) , key = reverse, to sort reverse the sorting order, key=len, to sort based on the length

