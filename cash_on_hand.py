from pathlib import Path
import csv

# Create a file path to the CSV file
file_path = [Path.cwd() /"csv_reports"/"cash on hand (1).csv"]

# Create an empty list for cash on hand records
cashonhand = []

# Read the CSV file
for fp in file_path:
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        # Append delivery records to the cash on hand list
        for row in reader:
            cashonhand.append([row[0], row[1]])

# print(cashonhand)

# Scenario 1 
# Print the required output format          
print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

# Create dictionaries to respective previous value, cash surplus and the day 
previous_value = 0
highest_surplus = 0
highest_surplus_day = 0

# Record of cashonhand and convert the the value to a float in the same time
for record in cashonhand:
    current_day = record[0]
    current_value = float(record[1])

    #Calculate the surplus for cashonhand 
    if current_value > previous_value:
        surplus = current_value - previous_value

    # Find out if the value of the current day is higher than the previous day
        if surplus > highest_surplus:
            highest_surplus_day = current_day
            highest_surplus = surplus
    previous_value = current_value

print(f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: SGD{int(highest_surplus)}")



# Scenario 2
# print the required output format:
print(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")

# Create  dictionaries to respective previous value, cash deficits and the day 
previous_value = 0
highest_cash_deficit = 0 
highest_deficit_day = 0

# Record of cash on hand and convert the value to a float in the same time
for record in cashonhand:
    current_day = record[0]
    current_value = float(record[1])

    # Calculate the deficits for the cashonhand
    if current_value < previous_value:
        deficit = previous_value - current_value

    # Find out the value of the current day is higher than the previous day
        if deficit > highest_cash_deficit:
            highest_deficit_day = current_day
            highest_cash_deficit = deficit 
    previous_value = current_value

print(f"[HIGHEST CASH DEFICIT] DAY: {highest_deficit_day}, AMOUNT: SGD{int(highest_cash_deficit)}")


# Scenario 3
# Create  dictionaries to respective previous value, cash deficits 
previous_value = 0
deficits = []

# Record of cash on hand and convert the value to a float in the same time 
for record in cashonhand:
    current_day = record[0]
    current_value = float(record[1])
# Calculate the deficits for the cash on hand 
    deficit = previous_value - current_value
# Print the deficit values that is higher than the previous day 
    if current_value < previous_value:
        deficits.append({"day": current_day, "amount": deficit})
        print(f"[CASH DEFICIT] DAY: {current_day}, AMOUNT: SGD{int(deficit)}")
    previous_value = current_value

# Sort the top3 deficits based on amount
def get_deficit_amount(value):
    return value ["amount"]
cashonhand_deficit = sorted(deficits, key=get_deficit_amount, reverse=True)

# Print out the top3 HIGHEST CASH DEFICITS
# The highest cash deficit
highest_deficit = cashonhand_deficit[0]
print(f"[HIGHEST CASH DEFICIT] DAY: {highest_deficit['day']}, AMOUNT: SGD{int(highest_deficit['amount'])}")

# 2nd highest cash deficit
second_deficit = cashonhand_deficit[1]
print (f"[2ND HIGHEST CASH DEFICIT] DAY: {second_deficit['day']}, AMOUNT: SGD {int(second_deficit['amount'])}")

# 3rd highest cash deficit
third_deficit = cashonhand_deficit[2]
print(f"[3RD HIGHEST CASH DEFICIT] DAY: {third_deficit['day']}, AMOUNT: SGD{int(third_deficit['amount'])}")