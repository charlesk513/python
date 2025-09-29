
def Fahrenheit(temperature):
    result = (temperature * (9/5)) + 32
    print(f"The temperature {temperature}C is {result}F.")
    return result


def Celsius(temperature):
    result = (temperature - 32)* (5/9)
    print(f"The temperature {temperature}F is {result}C.")
    return result

print("The temperature units converter")

while(1):
    print("Conversion options")
    print("1. Convert from Celsius to fahrenheit")
    print("2. Convert from fahrenheit to Celsius")

    choice = int(input("Enter choice 1 or 2: "))
    temperature = int(input("Enter the temperature to convert: "))
    if choice == 1:
        Fahrenheit(temperature)
    elif choice == 2:
        Celsius(temperature)
    else:
        print("Choice entered not among options")
