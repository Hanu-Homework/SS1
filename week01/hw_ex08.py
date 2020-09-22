def calculate_mpg(miles: int, gallons: int) -> int:
    return miles * gallons


number_of_miles = int(input("Enter the number of miles: "))
number_of_gallons = int(input("Enter the number of gallons of gas used: "))

print(f">> MPG: {calculate_mpg(number_of_miles, number_of_gallons)}")
