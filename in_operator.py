# The IN Operator helps to compare one variable agaisnt an array, list, dictionary or set.

# For a list:

# names = input("Choose one name among the list:")
# options = ["Ali", "Abu", "Ann"]
# if names in options:
#     print("Correct, the name is found among the list!")
    
# else:
#     print("Name not found in the list!")
    
    
# For a Dictionary:

# key = "name"
# person = {
#     "name":"Ali",
#     "profession": "Teacher",
#     }

# if key in person:
#     print("Name is a valid dictionay key in the person object")

# For set:

names = {"Ann", "Abu", "Ali"}
if "Ann" in names:
    print("Ann is found in the set!")