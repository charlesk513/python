# from calcmod import sum, difference, product, quotient, modulus, squareroot
import calcmod
first = 1
print("\nReliable calculator, solving your arithmetic problems.\n")

print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Square root (#)")
print("6. Modulus (%)\n")

while(1):
    
    if(first):
        choice = input("Please enter the operator ('+', '-', '*', '/' , '%' , '#'): ")
        numberOne = float(input("\nEnter the first number: "))
        numberTwo = float(input("Enter second number: "))
    else:
        print(f"The answer stored is {result}")
        numberOne = result
        choice = input("Please enter the operator ('+', '-', '*', '/' , '%' , '#'): ")          
        numberTwo = float(input("Enter second number: "))
        
    if choice in ['+', '-', '*', '/' , '%' , '#']:
        try:
            
            if choice == '+':
                result = calcmod.sum(numberOne, numberTwo)
                print(f"The operation {numberOne} + {numberTwo} = {numberOne + numberTwo}")
            elif choice == '-':
                result = calcmod.difference(numberOne, numberTwo)
                print(f"The operation {numberOne} - {numberTwo} = {numberOne - numberTwo}")
            elif choice == '*':
                result = calcmod.product(numberOne, numberTwo)
                print(f"The operation {numberOne} * {numberTwo} = {numberOne * numberTwo}")
            elif choice == '/':
                if numberTwo != '0':
                    result = calcmod.quotient(numberOne, numberTwo)
                    print(f"The operation {numberOne} / {numberTwo} = {numberOne / numberTwo}")
                else:
                    print("Mathematical error, division by zero!")   
            elif choice == '#':
                result = calcmod.squareroot(numberOne)
                print(f"The square root of {numberOne} = {numberOne ** (0.5)}")
                
            elif choice == '%':
                result = calcmod.modulus(numberOne, numberTwo)
                print(f"The modulus of {numberOne} % {numberTwo} = {numberOne % numberTwo}")
        except ValueError:
            print("You've entered the wrong operand!")
        
    print("\nOperations\n")    
    print("1. New operation")
    print("2. Continue with the last result")
    
    permission = int(input("Choose an option from 1,2: "))
    if permission == 1:
        first = 1
    elif permission == 2:
        first = 0
    else:
        print("Option entered is not among options")
        break

print("Thanks for the cooperation and love to use this calculator")
