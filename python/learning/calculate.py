print("Calculator")
print("operators")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square root")

choice = input("Make a choice of the operator (1/2/3/4/5): ")

if choice in ['1', '2', '3', '4', '5']:
    try:
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        if choice == '1':
            print(f"The operation {number1} + {number2} = {number1 + number2}")
        elif choice == '2':
            print(f"The operation {number1} - {number2} = {number1 - number2}")
        elif choice == '3':
            print(f"The operation {number1} * {number2} = {number1 * number2}")
        elif choice == '4':
            if number2 != '0':
                print(f"The operation {number1} / {number2} = {number1 / number2}")
            else:
                print("Mathematical error, division by a zero")
        elif choice == '5':
            print(f"The operation {number1} ^ (1/2) = {pow(number1,(1/2))}")
        else:
            print("Please enter the right operand!")
    except ValueError:
        print("invalid input, option out of range!")
else:
    print("invalid input, option out of range!")