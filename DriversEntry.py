#Description: Final Sprint Project 2. MAIN MENU for HAB Taxi Company services. A program that allows
#             the Employee's info to be entered and stored.
#             
#Author: Group 8
#Dates: July 31st, 2024



#Program Libraies

import datetime
import time


# Program Constants
CURR_DATE = datetime.datetime.now()

def read_defaults():
    with open("Defaults.dat", "r") as f:
        return {
            "TRANS_NUM": f.readline().strip(),
            "NEXT_DRIVER": int(f.readline().strip()),
            "STAND_FEE": float(f.readline().strip()),
            "DAILY_RENT": float(f.readline().strip()),
            "WEEKLY_RENT": float(f.readline().strip()),
            "HST_RATE": float(f.readline().strip())
        }

# Helper functions
def FDate(userdate):
    day = int(userdate[0:2])
    month = int(userdate[3:5])
    year = int(userdate[6:10])
    return datetime.datetime(year, month, day)

def FDateS(DateValue):
    return DateValue.strftime("%Y-%m-%d")

def ValidEmpty(object):
   #Validates an input to confirm field is not empty
   while True:
      print()
      variable = input(f"      Enter the employee's {object:20}                ").title()
      if variable == "":
         print (f"      Data Entry Error: {object} cannot be blank.")
      else:
         break
   return variable

def ValidBinary(object):
   #validates yes or no inputs
   while True:
      print()
      choice = input(f"      {object:25}                              ").upper()
      if choice != "Y" and choice != "N":
         print ("Data Entry Error: 'Y' or 'N' must be entered.")
      else:
         break
   return choice

def Progress():
    for i in range (51):
        print('\r[' + '*' * i + ' ' * (50 - i) + ']', end='')
        time.sleep(0.01)
    print()

def enter_driver():
    while True:
        print()
        print()
        print()
        print()
        print ("Complete all fields below.")
        print()
        print()
        while True:
            defaults = read_defaults()  # Make sure to call read_defaults() here
            driver_id = defaults["NEXT_DRIVER"]  # Set driver_id from NEXT_DRIVER
            
            # Collect driver information
            
            input1 = ("first name")
            fname_driver = ValidEmpty(input1)
            input2 = ("last name")
            lname_driver = ValidEmpty(input2)
            print()
            print("Enter the driver's address of residence:")
            input3 = ("Street")
            street_driver = ValidEmpty(input3)
            input4 = ("City")
            city_driver = ValidEmpty(input4)
            input5 = ("Province")
            prov_driver = ValidEmpty(input5)
            input6 = ("Postal Code")
            pcode_driver = ValidEmpty(input6)
            print()
            mail_diff = input("Hit return if the driver's mailing address is the same or 'Y' if different: ").upper()
            if mail_diff == "Y":
                input7 = ("Street")
                street_mail = ValidEmpty(input7)
                input8 = ("City")
                city_mail = ValidEmpty(input8)
                input9 = input("Province")
                prov_mail = ValidEmpty(input9)
                input10 = input("Postal Code")
                pcode_mail = ValidEmpty(input10)
                Mail_Add = [street_mail, city_mail, prov_mail, pcode_mail]
            else:
                street_mail = "Same as above"
                city_mail = "Same as above"
                prov_mail = "Same as above"
                pcode_mail = "Same as above"
                Mail_Add = "Mailing address same."
            print()
            input11 = ("cell phone number")
            driver_cell = ValidEmpty(input11)
            input12 = ("home phone number")
            driver_homep = ValidEmpty(input12)
            print()
            input13 =("Licence Number")
            driver_licence = ValidEmpty(input13)
            input14 = ("Expiry Date (MM/YY)")
            licence_exp = ValidEmpty(input14)
            input15 = ("insurance company")
            insur_comp = ValidEmpty (input15)
            input16 = ("insurance policy number")
            policy_num = ValidEmpty(input16)
            print()

            while True:
                owner_status = input("      Does the Driver own their own vehicle (Y/N): ").upper()
                if owner_status == "Y":
                    input17 = ("vehicle's colour")
                    owncar_colour = ValidEmpty(input17)
                    input18 = ("vehicle's model year")
                    owncar_year = ValidEmpty(input18)
                    input19 = ("vehicle's model")
                    owncar_model = ValidEmpty(input19)
                    input20 = ("vehicle's licence plate")
                    owncar_plate = ValidEmpty(input20)
                    break
                elif owner_status == "N":
                    owncar_colour = "N/A"
                    owncar_year = "N/A"
                    owncar_model = "N/A"
                    owncar_plate = "N/A"
                    break
                else:
                    print()
                    print("Entry must be 'N' or 'Y'.")

            while True:
                print()
                start_date = input("Enter the date of the Driver's start of employment (DD-MM-YYYY): ")
                try:
                    date_obj = FDate(start_date)
                    break
                except:
                    print("Entry must be a valid DD-MM-YYYY.")

            
            
            driver_name = fname_driver + " " + lname_driver
            Driver_Add = [street_driver, city_driver, prov_driver, pcode_driver]
            cell_dsp = (f"C:{driver_cell}")
            homep_dsp = (f"H:{driver_homep}")
            Driver_Phone = [cell_dsp, homep_dsp]
            Driver_Vehicle = [owner_status, owncar_colour, owncar_year, owncar_model, owncar_plate]
            start_date_str = FDateS(date_obj)

            
            print()
            print(f"-------------------------------------------------------------------------------")
            print(f"                           HAB TAXI SERVICES                                   ")
            print(f"                         New Employee Addition                                 ")
            print(f"-------------------------------------------------------------------------------")
            print(                                                                                  )
            print(f"        Start Date:                    {start_date_str}                        ")
            print(f"        Driver ID:                     {driver_id}                             ")
            print(                                                                                  )
            print(f"        Driver Information:                                                    ")
            print(f"        Driver Name:                   {driver_name}                           ")
            print(f"        Driver Licence:                {driver_licence}                        ")
            print(f"        Licence Expiry:                {licence_exp}                           ")
            print(f"        Insurance Provider:            {insur_comp}                            ")
            print(f"        Insurance Policy:              {policy_num}                            ")
            print(                                                                                  )
            print(f"-------------------------------------------------------------------------------")
            print(                                                                                  )
            print(f"    Phone Numbers:      Cell:{driver_cell}  Home:{driver_homep}                ")
            print(                                                                                  )
            print(f"    Address:                                                                   ")
            print(                                                                                  )
            print(f"                 Street:               {street_driver}                         ")
            print(f"                 City:                 {city_driver}                           ")
            print(f"                 Province:             {prov_driver}                           ")
            print(f"                 Postal C              {pcode_driver}                          ")
            print()
            print(f"    Mailing Address:                                                           ")
            print(                                                                                  )
            print(f"                 Street:               {street_mail}                           ")
            print(f"                 City:                 {city_mail}                             ")
            print(f"                 Province:             {prov_mail}                             ")
            print(f"                 Postal Code:          {pcode_mail}                            ")
            print()
            print(f"-------------------------------------------------------------------------------")
            print(f"        Driver Own Vehicle?   {owner_status}                                   ")
            print(f"        Vehicle Details:  {owncar_colour} {owncar_year} {owncar_model} {owncar_plate}  ")
            print(f"-------------------------------------------------------------------------------")
            print()
            print()
            print()
            entry_check = input ("Is the entry above correct? Enter 'Y' to save the data or 'N' to start over.").upper()
            if entry_check == "Y":
                break

            print()





        print ("Saving Employeee data...")
        Progress()
        print ("Save complete.")


        with open("drivers.dat", "a") as f:
            f.write(f"{driver_id}, {driver_name}, {Driver_Add}, {Mail_Add}, {Driver_Phone}, {driver_licence}, {licence_exp}, {insur_comp}, {policy_num}, {Driver_Vehicle}, {start_date_str}, 0.00 \n")

        # Update driver ID
        defaults["NEXT_DRIVER"] += 1
        with open("Defaults.dat", "w") as f:
            f.write(f"{defaults['TRANS_NUM']}\n{defaults['NEXT_DRIVER']}\n{defaults['STAND_FEE']}\n{defaults['DAILY_RENT']}\n{defaults['WEEKLY_RENT']}\n{defaults['HST_RATE']}")

        go_again = input ("Press 'Y' to enter another employee, or 'N' to return to the main menu.").upper()
        if go_again == 'N':
            break