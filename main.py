print("Hello user of the energy consumption calculator")
print("Let's begin the calculation\n")

appliance_name = input("What is the name of the calculating device?")
power_watts = float(input("What is its power rating in Watts?"))
hours_per_day = int(input("How many hours per day of use?"))
days_per_month = int(input("How many days of use per month?"))
kwh_price = float(input("What is the price per kWh? "))

#Daily consumption (kWh/day)

daily_consumption = (power_watts/1000) * hours_per_day

#Monthly consumption (kWh)

monthly_consumption = daily_consumption * days_per_month

#Monthly cost

monthly_cost = monthly_consumption * kwh_price 

print("\n----- Energy Consumption Report -----")
print(f"Appliance: {appliance_name}")
print(f"Daily consumption: {daily_consumption:.2f} kWh")
print(f"Monthly consumption: {monthly_consumption:.2f} kWh")
print(f"Estimated monthly cost: R${monthly_cost:.2f} (The price is in Brazilian Reais because the origin of this project is within Brazilian territory.)")