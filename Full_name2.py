# create a program where a user has to correctly input their full name
print("Welcome")
name = input("Please Enter Your Full Name: ") # Asks user to input their full name
if len(name) == 0: # You haven’t entered anything. Please enter your full name.”
    print("You haven't entered anything. Please enter your full name.") 

elif len(name) < 4: #“You have entered less than 4 characters. Please make sure that you have entered your name and surname.”
    print("Yor have entered less than 4 characters. Please make sure that you have entered your full name.")

elif len(name) > 25: #“You have entered more than 25 characters. Please make sure that you have only entered your full name.”
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

else: # Thank you for entering your name.
    print("Thank you for entering your name.")