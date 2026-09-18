#accesing value in dictionary there is two ways get() and name["key"]


dictionary_val={"saket":"mishra","yash":"mishra","Harish":"jha","ayush":"shukla"}

#for key,value in dictionary_val.items():
   # print(f"{key} -> {value}")
    
    

#print(dictionary_val["ayush"])
#clear

#print(dictionary_val.get("saket"))
#Nested Dictionary 

family={
    "mom":{"name":"gala","age":76},
    "dad":{"name":"dala","age":74}
    }



for name,information in family.items():
    print(f"family member is : {name} ")
    parent_name=f"name :{information["name"]}"
    parent_age=f"age :{information["age"]}"
    print(f"\n {parent_name}")
    print(f"\n {parent_age}")
    
