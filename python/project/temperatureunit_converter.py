class ConversionMethods():
    def Fahrenheit(temperature):
        result = (temperature * (9/5)) + 32
        print(f"The temperature {temperature}C is {result}F.")
        return result


    def Celsius(temperature):
        result = (temperature - 32)* (5/9)
        print(f"The temperature {temperature}F is {result}C.")
        return result

conversion_method = ConversionMethods
print("The temperature units converter")

while(1):
    print("Conversion options")
    print("1. Convert from Celsius to fahrenheit")
    print("2. Convert from fahrenheit to Celsius\n")

    choice = int(input("Enter choice 1 or 2: "))
    temperature = int(input("\nEnter the temperature to convert: "))
    if choice == 1:
        conversion_method.Fahrenheit(temperature)
    elif choice == 2:
        conversion_method.Celsius(temperature)
    else:
        print("Choice entered not among options\n")
