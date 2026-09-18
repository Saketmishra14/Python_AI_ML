
# def greet(name,age):
#     print(f"i Paulo! I am {name} and I am {age} Year Old.");
    
# count=0
# while count<10:
#     greet("saket",45)
#     count+=1

text="this is simple text and value is {}"
num=36
result=text.format(num)
print(result)
    
def formated_name(first_name,last_name):
    
    #this one is generate docstring
    """_summary_

    Args:
        first_name (_type_): _description_
        last_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    full_name=f"{first_name} {last_name}"
    return full_name.title()

name=formated_name("saket","mishra")

def multiply(a,b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a*b;

result = multiply(3,5)

# print(result)

#enumerate keyword : we can use indexes as value as well.

#pass : it used to run function without body