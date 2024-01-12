# Creating or writing new files in python

with open("writing_file.txt", 'w') as file:
    file.write("Hello from me to you...")
    
with open("writing_file.txt", 'a') as file:
    file.write("\nI would love you again and again!")
    file.write("\n\tI would love you again and again!")