#Tuple is immutable

#tuple is doesn't support item assignment

tuple_veg=("Lemon","potato")
# tuple_veg[0]="apple"

for veg in tuple_veg:
    print(veg)
    
    #Join Tuples
    
tuple1=("apple","mango","guava")
tuple2=(1,2,3)

tuple3=tuple1+tuple2
print(tuple3)

#conditional statement in python

temperature=60;

if temperature<45:
    print("Wear a jacket")
    
elif temperature<=60:
    print('Wear a T-shirt')

else:
    print("It's Rainy")

#hands on conditional statement if else

name=("bob","yash","saket")

if "saket" in name:
    print("Yash is registered")
else: print("yash is not registered")


activities=("sports","gokarting","basketball")
group_interest=("cricket","standup comedy","singing")

if "sports" in activities and ("cricket" in group_interest or "comedy" in group_interest):
    print("person like sports criket")
else: print("person is not interested")
#del name
print(name)







