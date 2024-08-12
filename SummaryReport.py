#Description: Final Sprint Project 2. Option 8 in Main Menu, Summary Report
#             
#Author: Group 8
#Dates: Aug 5-12, 2024


from DriverUtils import parse_driver_record


def summary_report():
    # Initialize counters and accumulators
    total_employees = 0
    total_owners = 0
    total_revenue = 0.0
    total_expenses = 0.0
    total_balance_due = 0.0

    # Process Employee file
    with open("Drivers.dat", "r") as emp_file:
        for record in emp_file:
            try:
                driver_data = parse_driver_record(record)
            except ValueError as ve:
                print(f"Error processing record: {record}")
                print(ve)
                continue

            total_employees += 1
            total_balance_due += driver_data["bal_due"]

            if driver_data["owner_car"][1] == "Y":
                total_owners += 1

    # Process Revenue file
    with open("Revenue.dat", "r") as rev_file:
        for record in rev_file:
            parts = record.strip().split(", ")
            trans_amt = float(parts[4])
            total_revenue += trans_amt

    # Process Expenses file
    with open("Expenses.dat", "r") as exp_file:
        for record in exp_file:
            parts = record.strip().split(", ")
            trans_amt = float(parts[4])
            total_expenses += trans_amt

    # Calculate net profit/loss
    net_profit_loss = total_revenue - total_expenses

    # Display the summary report
    print("\nHAB Taxi Services - Summary Report")
    print("=" * 40)
    print(f"Total Number of Employees: {total_employees}")
    print(f"Total Number of Employees who own cars: {total_owners}")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Expenses: ${total_expenses:,.2f}")
    print(f"Net Profit/Loss: ${net_profit_loss:,.2f}")
    print(f"Total Balance Due from Employees: ${total_balance_due:,.2f}")
    print("=" * 40)

# Call the summary report function for Option 8
# summary_report()