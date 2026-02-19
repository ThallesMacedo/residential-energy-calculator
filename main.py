import json
from services import (
    add_appliance,
    view_report,
    remove_appliance,
    update_appliance
)

from storage import load_data

#Welcome to the program.
print("\nHello user of the energy consumption calculator")
print("Let's begin the calculation\n")

#Function: Main
def main():
    appliances = load_data()

    while True:
        print('\n===== Energy Consumption Calculator =====\n1 - Add appliance \n2 - View report \n3 - Remove appliance \n4 - Edit appliance \n5 - Exit')
        choise = input('Choose an option:')
        
        #Add appliance
        if choise == '1':
            add_appliance(appliances)
        
        #View report
        elif choise == '2':
           view_report(appliances)

        #Remove appliance          
        elif choise == "3":
            remove_appliance(appliances)

        #Edit appliance
        elif choise == "4":
            update_appliance(appliances) 

        #Exit
        elif choise == '5':
            break
        
        #validation menu
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")
            
if __name__ == "__main__":
    main()