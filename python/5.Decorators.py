#decorators are used to change the behavoir of the existing funcitons without actually changing the source code of it


def div(a,b):
    print(a/b)

def smart_div(func): #taking function as an argument

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smart_div(div) 
div1(2,4) 

# here we want the bigger value to be numerator so we are chagning the div function without actually changing
