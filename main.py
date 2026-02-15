#Welcome to the program.
print("Hello user of the energy consumption calculator")
print("Let's begin the calculation\n")

#Function: Validate Float values ​​for inputs.
def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print('Invalid input. Please enter a valid number.')

#Function: Validate Int values ​​for inputs.
def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Invalid input. Please enter a valid number.')

#Function: Energy consumption calculation formula
def calculate_energy():
    appliance_name = input("What is the name of the calculating device? ")
    power_watts = get_float_input('What is its power rating in Watts? ')
    hours_per_day = get_int_input('How many hours per day of use? ')
    days_per_month = get_int_input('How many days of use per month? ')
    kwh_price = get_float_input('What is the price per kWh? ')

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
    print("\n-----------------------------------")

    return appliance_name, monthly_consumption, monthly_cost

#Function: Main
def main():
    appliances = []  # Made List

    while True:
        print('===== Energy Consumption Calculator =====\n1 - Add appliance \n2 - View report \n3 - Exit')
        choise = input('Choose an option:')
        if choise == '1':
            
            name, consumption, cost = calculate_energy()

            appliances.append({
            "appliance_name": name,
            "monthly_consumption": consumption,
            "monthly_cost": cost
                               })
        elif choise == '2':
            if not appliances:
                print('The list is empty.')
            else:
                for appliance in appliances:
                    print(f"\nAppliance: {appliance['appliance_name']}")
                    print(f"Monthly Consumption: {appliance['monthly_consumption']:.2f} kWh")
                    print(f"Monthly Cost: R${appliance['monthly_cost']:.2f}\n")

        elif choise == '3':
            break
            

#total_consumption = sum(a["monthly_consumption"] for a in appliances)
#total_cost = sum(a["monthly_cost"] for a in appliances)

#print("\n===== HOUSE TOTAL =====") ""
#print(f"Total Monthly Consumption: {total_consumption:.2f} kWh")
#print(f"Total Estimated Cost: R${total_cost:.2f}")
#print("========================")

if __name__ == "__main__":
    main()

