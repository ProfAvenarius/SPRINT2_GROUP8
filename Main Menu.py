#Description: Final Sprint Project 2. MAIN MENU for HAB Taxi Company services. A program that offers 
#             the user a selection of options 
#Author: Group 8
#Dates: July 31st, 2024



#Program Libraries


import datetime


#Program constants


#Program Functions



def MenuDSP ():

    Choices = ['1','2','3','4','5','6','7','8','9','10']

    print()
    print()
    print()
    print (f"                                       HAB Taxi Services ")
    print (f"                                    Company Services System ")
    print()
    print()
    print (f"                                1. Enter a New Employee (driver). ")
    print (f"                                2. Enter Company Revenues. ")
    print (f"                                3. Enter Company Expenses. ")
    print (f"                                4. Track Car Rentals. ")
    print (f"                                5. Record Employee Payment. ")
    print (f"                                6. Print Company Profit Listing. ")
    print (f"                                7. Print Driver Financial Listing. ")
    print (f"                                8. Corporate Summary Report. ")
    print (f"                                9. Quit Program. ")
    print()
    print()
    while True:
        choice = input ("                          Enter choice (1-9): ")
        if choice not in Choices:
            print ("User Input Error: Entry must be 1 - 9")
        else:
            break

    return choice


# Function to add a new employee
def add_employee():
    driver_number = input("Enter driver number: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")
    license_number = input("Enter driver's license number: ")
    license_expiry_date = input("Enter license expiry date (YYYY-MM-DD): ")
    insurance_company = input("Enter insurance policy company: ")
    policy_number = input("Enter policy number: ")
    own_car = input("Does the driver have their own car? (Yes/No): ")
    balance_due = float(input("Enter balance due: "))
    
    print(f"Employee added: {driver_number}, {name}, {address}, {phone_number}, {license_number}, {license_expiry_date}, {insurance_company}, {policy_number}, {own_car}, {balance_due:.2f}")

# Function to add a revenue record
def add_revenue():
    transaction_id = input("Enter transaction ID: ")
    transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    description = input("Enter description: ")
    driver_number = input("Enter driver number: ")
    amount = float(input("Enter amount: "))
    hst = float(input("Enter HST: "))
    total = float(input("Enter total: "))
    
    print(f"Revenue added: {transaction_id}, {transaction_date}, {today_date}, {description}, {driver_number}, {amount:.2f}, {hst:.2f}, {total:.2f}")

# Function to add an expense record
def add_expense():
    invoice_number = input("Enter invoice number: ")
    invoice_date = input("Enter invoice date (YYYY-MM-DD): ")
    driver_number = input("Enter driver number: ")
    item_number = input("Enter item number: ")
    description = input("Enter description: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    item_total = float(input("Enter item total: "))
    subtotal = float(input("Enter subtotal: "))
    hst = float(input("Enter HST: "))
    total = float(input("Enter total: "))
    
    print(f"Expense added: {invoice_number}, {invoice_date}, {driver_number}, {item_number}, {description}, {cost:.2f}, {quantity}, {item_total:.2f}, {subtotal:.2f}, {hst:.2f}, {total:.2f}")

# Main Program
while True:
    menu_option = display_menu()
    
    if menu_option == '1':
        add_employee()
    elif menu_option == '2':
        add_revenue()
    elif menu_option == '3':
        add_expense()
    elif menu_option == '9':
        print("Exiting program...")
        break
    else:
        print("Option not implemented yet.")






menu_opt = MenuDSP()

print (menu_opt)
