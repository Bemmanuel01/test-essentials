# To read type of files in python simply use the following format:

# with open('filename', 'r') a file:
#     print(file.read())

# with open('merge-conflict.txt', 'r') as file:
#     print(file.read())

with open('not_operator.py', 'r') as file:
    content = file.read()
    
print("content", content)

    