def to_fahrenheit(celcius):
    return celcius * 9 / 5 + 32


c = int(input("Enter the celcius: "))
print(f">> Fahrenheit: {to_fahrenheit(c)}")
