my_list=["saket","varsha","payal","aaradhya","anushka"]


def my_function(name):
    for i in name:
        result=f"I am {i}"
        print(result)
        
my_function(name=my_list)


def multiple_return(a,b):
    return a*b,1,"this is string"

a,b,c=multiple_return(4,5);
print(a)
print(c)
print(b)