from random import randint
from random import choice

items=["apple","banana","mangoes","cherry"]


def rand_fruits(fruits):
    rand=randint(a=0,b=len(fruits)-1)
    single_fruit=fruits[rand]
    print(single_fruit)


rand_fruits(items)
# print(randint(a=44,b=55))


# choice
