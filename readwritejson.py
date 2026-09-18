import json

from pathlib import Path

# names=["saket","kumar","mishra"]
# with Path.open('names.json','w') as file:
#     content=json.dumps(names)
#     file.write(content)
    
with Path.open('names.json','r') as file:
    content=json.load(file)
    print(content)