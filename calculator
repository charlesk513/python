def calculator():
    print("\nReliable calculator, solving your arithmetic problems.\n")
    
    name = input("write your name please: ")
    
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square root (**(1/2))")
    print("6. Modulus (%)\n")

    choice = input("Please enter the operator (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5','6']:
        try:
            numberOne = float(input("\nEnter the first number: "))
            numberTwo = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"The operation {numberOne} + {numberTwo} = {numberOne + numberTwo}")
            elif choice == '2':
                print(f"The operation {numberOne} - {numberTwo} = {numberOne - numberTwo}")
            elif choice == '3':
                print(f"The operation {numberOne} * {numberTwo} = {numberOne * numberTwo}")
            elif choice == '4':
                if numberTwo != '0':
                    print(f"The operation {numberOne} / {numberTwo} = {numberOne / numberTwo}")
                else:
                    print("Mathematical error, division by zero!")   
            elif choice == '5':
                print(f"The square root of {numberOne} = {numberOne ** (numberTwo/2)}")
            elif choice == '6':
                print(f"The modulus of {numberOne} % {numberTwo} = {numberOne % numberTwo}")
        except ValueError:
            print("You've not entered the an operand!")
    else:
        print("The choice chosen is not among the alternatives given, try again!")
        
# print(f"Congraturations {name}, enjoy your time!")
calculator()

