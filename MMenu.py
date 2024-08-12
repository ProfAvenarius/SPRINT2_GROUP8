## Description: Final Sprint Project 2. MAIN MENU for HAB Taxi Company services. A program that offers 
#              the user a selection of options 
# Author: Group 8
# Dates: July 31st, 2024

# Program Libraries
import datetime

# Program Functions
def MenuDSP():
    Choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    print()
    print(f"                                       HAB Taxi Services ")
    print(f"                                    Company Services System ")
    print()
    print(f"                                1. Enter a New Employee (driver). ")
    print(f"                                2. Enter Company Revenues. ")
    print(f"                                3. Enter Company Expenses. ")
    print(f"                                4. Track Car Rentals. ")
    print(f"                                5. Record Employee Payment. ")
    print(f"                                6. Print Company Profit Listing. ")
    print(f"                                7. Print Driver Financial Listing. ")
    print(f"                                8. Corporate Summary Report. ")
    print(f"                                9. Quit Program. ")
    print()
    
    while True:
        choice = input("                          Enter choice (1-9): ")
        if choice not in Choices:
            print("User Input Error: Entry must be 1 - 9")
        else:
            return choice