
num=0

while num<5:
    print(num)
    num +=1
    
    
    
prompt = "Enter 'Quit' To end the program";
prompt += "\nEnter Your command:"


while True:
    command=input(prompt)
    if command=='quit':
        break; #exit this loop
    else:
        print(f"you Enter This command : {command}")

print(prompt)