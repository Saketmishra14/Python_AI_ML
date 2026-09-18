from pathlib import Path
# Exception handling

try:
    print(12/6);
except ZeroDivisionError as e:
    print(f"error ocurred {e}")
else:
    print("Everything is well!!")
finally:
    #code to clean up resources 
    print("what ever happen i'll  executed")
    
    
path=Path('example.txt')

try:
    content=path.read_text()
    print(content)
except FileNotFoundError as r:
    print(f"error occur :{r}")

 