# Description: Final Sprint Project 2. This file produces the Drivers Financial Listing
# Author: Group 8
# Dates: July 31st - Aug. 12, 2024

# Program Libraries

import datetime
import time
from DriverUtils import parse_driver_record

# Program Constants
CURR_DATE = datetime.datetime.now()

# Program functions:

def parse_drivers_file(file_path):
    driver_list = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                try:
                    driver_data = parse_driver_record(line)
                    driver_list.append((driver_data["driver_name"], driver_data["driver_id"]))
                except ValueError as e:
                    print(f"Error parsing record: {e}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    
    return driver_list

def parse_revenue_file(filename, search_driver_id):
    results = []
    total_transactions = 0
    total_amount = 0.0
    total_hst = 0.0
    total_sum = 0.0

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            parts = line.split(',')  # Assuming the fields are separated by commas
            
            if len(parts) < 7:  # Make sure there are enough fields
                continue  # Skip lines that don't have the expected number of fields
            
            driver_id = parts[3].strip()
            
            if driver_id == search_driver_id:
                # Extract relevant fields
                transaction_id = parts[0].strip()
                date = parts[1].strip()
                descrip = parts[2].strip()
                trans_amt = float(parts[4].strip())  # Convert to float
                hst_amt = float(parts[5].strip())    # Convert to float
                trans_tot = float(parts[6].strip())  # Convert to float
                
                # Add to accumulators
                total_transactions += 1
                total_amount += trans_amt
                total_hst += hst_amt
                total_sum += trans_tot
                
                # Format the output with proper spacing
                results.append(f"     {transaction_id:<15}   {date:<15}    {descrip:<30}   {trans_amt:<15.2f}     {hst_amt:<15.2f}  {trans_tot:<15.2f}")
    
    return results, total_transactions, total_amount, total_hst, total_sum

def FDate(userdate):
    day = int(userdate[0:2])
    month = int(userdate[3:5])
    year = int(userdate[6:10])
    return datetime.datetime(year, month, day)



def MainList():
    while True:
        print()
        print()
        print()
        print(f"-------------------------------------------------------------------------------")
        print(f"                           HAB TAXI SERVICES                                   ")
        print(f"                       Drivers Financial Listing                                ")
        print(f"-------------------------------------------------------------------------------")
        print()
        print()
        print()
        info_list = input("Would you like to review a list of all drivers names and ID's (Y/N)?   ").upper()
        print()
        print()
        print()
        if info_list == "Y":
            drivers_index = parse_drivers_file("Drivers.dat")
            print(f"{'Driver ID':<15}{'Driver Name'}")
            print("-" * 30)
            for driver in drivers_index:
                driver_id, driver_name = driver
                print(f"{driver_id:<15}{driver_name}")

        search_id = input("Enter a DriverID:  ")
        revenue_records, total_transactions, total_amount, total_hst, total_sum = parse_revenue_file("Revenue.dat", search_id)

        print("Transaction ID  |  Transaction Date  |  Transaction Description  |  Transaction Amount  | Transaction HST  |  Total")
        print("=" * 120)
        print("\n".join(revenue_records))  # Join records with newline characters

        print()
        print(f"Total Number of Transactions: {total_transactions}")
        print(f"Total Amount: ${total_amount:.2f}")
        print(f"Total HST: ${total_hst:.2f}")
        print(f"Total Sum: ${total_sum:.2f}")
        print()
        print()
        print()
        keep_going = input ("Press 'Y' to enter another employee, or 'N' to return to the main menu.").upper()
        if keep_going == 'N':
            break