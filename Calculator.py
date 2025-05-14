#simple AL calculations program
#doing addition between two numbers
def Plusal(a, b):
    return a + b
#doing subtraction between two numbers
def Minal(a, b):
    return a - b
#doing multiplication between two numbers
def Multiple(a, b):
    return a * b
#doing division between two numbers
def Dividal(a, b):
    return a / b
#to print the operation names
print("Select Arithmetic operation:\n")
print("1.Plusal","(add)")
print("2.Minal","(subtract)")
print("3.Multiple","(multiply)")
print("4.Dividal","(divide)")
while True:
#to take the input from the user
    choice = input("Enter the choice(1/2/3/4):")
#to choose one of the four operations
    if choice in('1','2','3','4'):
        try:
            num1 = float(input("Enter first value:"))
            num2 = float(input("Enter second value:"))
        except ValueError:
            print ("Invalid input.Please enter number.")
            continue
        if choice == '1':
            print(num1,"+", num2, "=", Plusal(num1,num2))
        elif choice == '2':
            print(num1,"-", num2, "=", Minal(num1,num2))
        elif choice == '3':
            print(num1,"*", num2, "=", Multiple(num1,num2))
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:    
                print(num1,"/", num2,  "=", Dividal(num1, num2))
#to take the next calculation if the user wants
#break the loop if the user's answer in "cancel"
        next_calculation = input("Let's do next calculation? (ok/cancel):")
        if next_calculation == "cancel":
            break
    else:
        print("invalid Input")
