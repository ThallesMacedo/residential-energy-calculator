from utils import get_float_input, get_int_input
from storage import save_data

#Function: Energy consumption calculation formula
def calculate_energy():

    appliance_name = input("\nWhat is the name of the calculating device? ")
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

#Function: Add Appliance
def add_appliance(appliances):
    name, consumption, cost = calculate_energy()

    appliances.append({
            "appliance_name": name,
            "monthly_consumption": consumption,
            "monthly_cost": cost
                               })
    save_data(appliances)

#Function: View Report
def view_report(appliances):
    if not appliances:
        print('\nThe list is empty.\n')
        return

    print("\n===== ENERGY REPORT =====")
    for appliance in appliances:
        print(f"\nAppliance: {appliance['appliance_name']}")
        print(f"Monthly Consumption: {appliance['monthly_consumption']:.2f} kWh")
        print(f"Monthly Cost: R${appliance['monthly_cost']:.2f}\n")
        print("==========================\n")

    total_consumption = sum(appliance["monthly_consumption"] for appliance in appliances)
    total_cost = sum(appliance["monthly_cost"] for appliance in appliances)

    print("\n===== HOUSE TOTAL =====")
    print(f"Total Monthly Consumption: {total_consumption:.2f} kWh")
    print(f"Total Estimated Cost: R${total_cost:.2f}")
    print("========================")

    print("\n===== HIGHER ELECTRICITY CONSUMPTION =====")

    highest_consumption = max(
        appliances,
        key=lambda appliance: appliance["monthly_consumption"]
    )

    print(f"Appliance: {highest_consumption['appliance_name']}")
    print(f"Monthly Consumption: {highest_consumption['monthly_consumption']:.2f} kWh")

    print("\n===== HIGHER ELECTRICITY COST =====")

    highest_cost = max(
        appliances,
        key=lambda appliance: appliance["monthly_cost"]
    )

    print(f"Appliance: {highest_cost['appliance_name']}")
    print(f"Highest Monthly Cost: R${highest_cost['monthly_cost']:.2f}")

    print("========================")

#Function: Remove appliance
def remove_appliance(appliances):
    if not appliances:
        print("\nNo appliances to remove.")
        return

    for i, ordem in enumerate(appliances, start=1):
        print(f"\n{i}: {ordem['appliance_name']} - {ordem['monthly_consumption']:.2f} KWH - R${ordem['monthly_cost']:.2f}")
    number = get_int_input("\nWhich appliance should I remove?" )
    if 1 <= number <= len(appliances):
        removed = appliances.pop(number-1)
        save_data(appliances)
        print(f"\n{removed['appliance_name']} removed successfully.")
    else:
        print("\nInvalid number.")

#Function: Edit appliance
def update_appliance(appliances):
    if not appliances:
        print("\nNo appliances to update.")
        return

            
    for i, ordem in enumerate(appliances, start=1):
        print(f"\n{i}: {ordem['appliance_name']} - {ordem['monthly_consumption']:.2f} KWH - R${ordem['monthly_cost']:.2f}")
    numberedit = get_int_input("\nWhich device should I update?" )
            
    if 1 <= numberedit <= len(appliances):
        appliance = appliances[numberedit - 1]
        print(f"\nEditing {appliance['appliance_name']}")

        # Request new values
        new_name = input("New name: ")
        new_power = get_float_input("New power (Watts): ")
        new_hours = get_int_input("New hours per day: ")
        new_days = get_int_input("New days per month: ")
        new_price = get_float_input("New kWh price: ")

        # Recalculate
        daily = (new_power / 1000) * new_hours
        monthly = daily * new_days
        cost = monthly * new_price

        # Update dictionary
        appliance["appliance_name"] = new_name
        appliance["monthly_consumption"] = monthly
        appliance["monthly_cost"] = cost

        save_data(appliances)

        print("\nAppliance updated successfully!")

    else:
        print("Invalid input. Please enter a valid number.")