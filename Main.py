# Description: Final Sprint Project 2. MAIN for HAB Taxi Company services. A program that serves 
#              as a framework for a number of business functions, accessible through a menu.
# Author: Group 8
# Dates: Aug 1st, 2024

# Program Libraries
import datetime
import time
import DriversEntry
import SummaryReport
import MMenu
from DriverUtils import parse_driver_record
from DriverUtils import Progress
# Program Constants
CURR_DATE = datetime.datetime.now()
records = []

f = open('Defaults.dat', 'r')

NEXT_TRANS = int(f.readline())
NEXT_DRIVER = int(f.readline())
STAND_FEE = float(f.readline())  # Monthly stand fee
DAILY_RENTAL = float(f.readline())  # Daily rental fee
WEEKLY_RENTAL = float(f.readline())  # Weekly rental fee
HST_RATE = float(f.readline())


f.close()



#Program Functions




def update_driver_record(record_dict):
    # Format the record back to the original format for writing back to the file
    return f"{record_dict['driver_id']}, {record_dict['driver_name']}, {record_dict['Driver_Add']}, {record_dict['mail_add']}, {record_dict['driver_phone']}, {record_dict['driver_licence']}, {record_dict['driver_exp']}, {record_dict['insur_comp']}, {record_dict['insur_policy']}, {record_dict['owner_car']}, {record_dict['start_date']}, {record_dict['bal_due']:.2f}"


def append_revenue_record(driver_id, stand_fee):
    trans_id = NEXT_TRANS
    trans_date = CURR_DATE.strftime("%Y-%m-%d")
    trans_description = "Monthly Stand Fee"
    hst_amt = stand_fee * HST_RATE
    trans_total = stand_fee + hst_amt
    
    revenue_record = f"{trans_id}, {trans_date}, {trans_description}, {driver_id}, {stand_fee:.2f}, {hst_amt:.2f}, {trans_total:.2f}"
    
    with open('Revenue.dat', 'a') as rev_file:
        rev_file.write(revenue_record + "\n")






#MAIN Program

today_is = "1"#CURR_DATE.strftime("%d")

if today_is == "1":
        print()
        print()
        print()
        print ("Today is the 1st of the month and Stand Fees are being processed...")
        Progress()
        print ("Revenue file updated successfully.")
        print ("Employee balances updated successfully.")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        with open('Drivers.dat', 'r') as e:
                for DriveRecord in e:
                        try:
                                driver_data = parse_driver_record(DriveRecord)
                        except ValueError as ve:
                                print(f"Error processing record: {DriveRecord}")
                                print(ve)
                                continue
        
        # Check if the driver owns a car
                        if driver_data["owner_car"][1] == "Y":
                                driver_data["bal_due"] += (STAND_FEE * (1+HST_RATE))
                                append_revenue_record(driver_data["driver_id"], STAND_FEE)
                                NEXT_TRANS += 1
                        
                        # Add the modified or unmodified record back to the list
                        records.append(update_driver_record(driver_data))

        # Write the updated records back to the file
                        with open('Drivers.dat', 'w') as e:
                                for record in records:
                                        e.write(record + "\n")







# Main Menu
print()
print()
print()
print()
while True:
    choice = MMenu.MenuDSP()  # Call MenuDSP from MMenu

    if choice == '1':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Enter a New Employee (driver).")
        DriversEntry.enter_driver()  # Replace some_function with the appropriate function in DriversEntry
        print("\n\n")

    elif choice == '2':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Enter Company Revenues.")
        # Implement the relevant code
        print("\n\n")

    elif choice == '3':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Enter Company Expenses.")
        # Implement the relevant code
        print("\n\n")

    elif choice == '4':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Track Car Rentals.")
        # Implement the relevant code
        print("\n\n")

    elif choice == '5':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Record Employee Payment.")
        # Implement the relevant code
        print("\n\n")

    elif choice == '6':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Print Company Profit Listing.")
        # Implement the relevant code
        print("\n\n")

    elif choice == '7':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Print Driver Financial Listing.")
        # Implement the relevant code
        print("\n\n")

    elif choice == '8':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Corporate Summary Report.")
        SummaryReport.summary_report()
        # Implement the relevant code
        print("\n\n")

    elif choice == '9':
        print()
        print()
        print()
        print()
        print(f"You have selected {choice}, Quit Program.")
        print("\n\n")
        break

    else:
        print("Invalid choice, please try again.")