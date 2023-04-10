import os.path

def calculator():
    num1 = input("Enter the first number:")
    num2 + input("Enter the second number:")

    operator = input("Enter an operator (+,-,*,/):")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Invalid input, please enter a number,")
     
calculator()
if operator =="+":result = num1 + num2
elif operator =="-": result = num1 - num2
elif operator =="*": result = num1 * num2
elif operator =="/": if num2 == 0:
print("Division by zero is not allowed.")
calculator()
    else:
        result = num1/num2
else:
    print("Invalid operator, plese enter one of these: +,-,*,/")
    calculator()
print(f"The result is: {result}")
with open("equations.txt", "a") as f:f.write(f"{num1}{operator}{num2}={result}\n")

def read_file():
    filename = input("Enter the name of the file:")
if not os.path.isfile(filename):
    print("File not found, please try again.")
    read_file()
else:
    with open(filename,"r") as f: equations = f.readlines() for equations in equations: 
        print(equation.strip())

print("Welcome to the calculator application!")
option= input("Enter 1 to perform a new calculation, or 2 to read from a file:")

if option == "1":
calculator()
elif option =="2":
    read_file()
else:
    print("Invalid option, please enter 1 or 2")