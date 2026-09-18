from pathlib import Path

content="Hii,Paulo Saket this side!\n"
content+= "i am adding the content inside the test file.\n"
content += "anything from your side then let me know."

path=Path('test.txt')

path.write_text(content)

#also use with keyword to read file and write

# path=Path('example.txt')

# if path.exists():
#     context =path.read_text()
#     print(context.title())
# else:
#     print("file doesn't exist.")
# st=path.name
# print(context.title())
