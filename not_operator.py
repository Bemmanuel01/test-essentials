# NOT Operator
# A type of conditional where you compare variables which are not 
# in another set, list or dictionary. example is as follows:


# my_name = False
# if not my_name:
#     print("Check-In with a different name!")
   
name = input("Enter your name: ")
if name not in ["John", "Ben", "Ali", "Ann"]:
    print("Check-In with a different name!")
        
else:
        print("Welcome, we're glad to have you!")
    
    