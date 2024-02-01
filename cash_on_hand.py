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

#print(cashonhand)

# Scenario 1 
# Print the required output format          
print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")


# Find out if the value of the current day is higher than the previous day
previous_value = 0
highest_surplus = 0
highest_surplus_day = 0

for record in cashonhand:
    current_day = record[0]
    current_value = float(record[1])
    
    if current_value > previous_value:
        surplus = current_value - previous_value

        if surplus > highest_surplus:
            highest_surplus_day = current_day
            highest_surplus = surplus
    previous_value = current_value

print(f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: SGD{highest_surplus}")



# Scenario 2
# print the required output format:
print(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")

# # find out if the value of the current day is lower than the previous day
previous_value = 0
highest_deficit = 0 
highest_deficit_day = 0

for record in cashonhand:
    current_day = record[0]
    current_value = float(record[1])

    if current_value < previous_value:
        deficit = previous_value - current_value

        if deficit > highest_deficit:
            highest_deficit_day = current_day
            highest_deficit = deficit 
    previous_value = current_value

print(f"[HIGHEST CASH DEFICIT] DAY: {highest_deficit_day}, AMOUNT: SGD{highest_deficit}")


# Scenario 3
# find out the value of the current data is lower or higher than the previous day
previous_value = 0
deficits = []
for record in cashonhand:
    current_day = record[0]
    current_value = float(record[1])

    deficit = previous_value - current_value
    
    if current_value < previous_value:
        deficits.append({"day": current_day, "amount": deficit})
        print(f"[CASH DEFICIT] DAY: {current_day}, AMOUNT: SGD{deficit}")
    previous_value = current_value

# Sort the top deficits based on amount (descending order)
def get_deficit_amount(value):
    return value ["amount"]
cashonhand_deficit = sorted(deficits, key=get_deficit_amount, reverse=True)

highest_deficit = cashonhand_deficit[0]
print(f"[HIGHEST CASH DEFICIT] DAY: {highest_deficit['day']}, AMOUNT: SGD{highest_deficit['amount']}")

# 2nd highest cash deficit
second_deficit = cashonhand_deficit[1]
print (f"[2ND HIGHEST CASH DEFICIT] DAY: {second_deficit['day']}, AMOUNT: SGD {second_deficit['amount']}")

# 3rd highest cash deficit
third_deficit = cashonhand_deficit[2]
print(f"[3RD HIGHEST CASH DEFICIT] DAY: {third_deficit['day']}, AMOUNT: SGD{third_deficit['amount']}")
