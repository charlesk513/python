i = 2   
number = int(input("Enter the number to test: "))
if number == 2:
    print("Its a prime number")
else:
    while i < number:
        modulus = number % i
        if modulus == 0:
            print(f"Divisible by {i} therefore not a prime number")
            break
        elif (i == (number-1)):
            print("Its a prime number")
        i += 1