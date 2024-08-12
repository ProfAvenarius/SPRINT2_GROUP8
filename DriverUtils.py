#Description: Final Sprint Project 2. This file houses functions that are called in multiple places causing 
#             potential conflicts.  
#Author: Group 8
#Dates: July 31st, 2024



#Program libraries
import time
import datetime


def parse_driver_record(record):
    # Formats Variables from comma seperated text files split by commas not inside brackets - To find lists nested in lists
    record = record.strip()
    parts = []
    temp = ''
    in_bracket = False
    
    for char in record:
        if char == '[':
            in_bracket = True
        elif char == ']':
            in_bracket = False
        elif char == ',' and not in_bracket:
            parts.append(temp.strip())
            temp = ''
            continue
        
        temp += char

    if temp:
        parts.append(temp.strip())
    
    if len(parts) != 12:
        raise ValueError(f"Unexpected number of fields: {len(parts)}")

    driver_id = parts[0].strip()
    driver_name = parts[1].strip()
    Driver_Add = parts[2].strip()
    mail_add = parts[3].strip()
    driver_phone = parts[4].strip()
    driver_licence = parts[5].strip()
    driver_exp = parts[6].strip()
    insur_comp = parts[7].strip()
    insur_policy = parts[8].strip()
    owner_car = parts[9].strip()
    start_date = parts[10].strip()
    bal_due = float(parts[11].strip())  # Convert bal_due to a float
    
    return {
        "driver_id": driver_id,
        "driver_name": driver_name,
        "Driver_Add": Driver_Add,
        "mail_add": mail_add,
        "driver_phone": driver_phone,
        "driver_licence": driver_licence,
        "driver_exp": driver_exp,
        "insur_comp": insur_comp,
        "insur_policy": insur_policy,
        "owner_car": owner_car,
        "start_date": start_date,
        "bal_due": bal_due,  
    }




def Progress():
    for i in range (51):
        print('\r[' + '*' * i + ' ' * (50 - i) + ']', end='')
        time.sleep(0.01)
    print()