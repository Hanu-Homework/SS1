amount = float(input("Enter the amount of purchase: "))

state_sales_tax = amount * 5 / 100
country_sales_tax = amount * 2.5 / 100
total_sales_tax = state_sales_tax + country_sales_tax
total_purchase = total_sales_tax + amount

print(f"Amount of purchase: {amount}")
print(f"State sales tax   : {state_sales_tax}")
print(f"Country sales tax : {country_sales_tax}")
print(f"Total sales tax   : {total_sales_tax}")
print(f"Total of purchase : {total_purchase}")
