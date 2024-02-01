from pathlib import Path
import csv

# create a file path to csv file
file_path = [Path.cwd()/"csv_reports"/"profit and loss (1).csv"]

# create an empty list for profit and loss record
profitandloss = []

# read the csv file
for fp in file_path:
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # append amount into the profit and loss record
        for row in reader:
            profitandloss.append([row[0], row[1], row[2], row[3], row[4]])

# print profit and loss after reading all files
# print(profitandloss)

# Scenario 1
# print the required output format
print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")

# find the value that is higher than the previous day
previous_value = 0
highest_surplus = 0
highest_surplus_day = 0

for record in profitandloss:
    current_day = record[0]
    current_value = float(record[4])

    if current_value > previous_value:
        surplus = current_value - previous_value
        
        if surplus > highest_surplus:
            highest_surplus_day = current_day
            highest_surplus = surplus
    previous_value = current_value
        
print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_surplus_day}, AMOUNT: SGD{highest_surplus}")

#Scenario2 
# print the required output format
print(f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")

# find the value that is lower than the previous day
previous_value = 0
highest_deficit = 0
highest_deficit_day = 0

for record in profitandloss:
    current_day = record[0]
    current_value = float(record[4])

    if current_value < previous_value:
        deficit = previous_value - current_value

        if deficit > highest_deficit:
            highest_deficit_day = current_day
            highest_deficit = deficit
    previous_value = current_value

    
print(f"[HIGHEST PROFIT DEFICIT] DAY {highest_deficit_day}, AMOUNT: SGD{highest_deficit}")


#Scenario 3
# find out the value of the current data is lower or higher than the previous day

previous_value = 0
deficits = []

for record in profitandloss:
    current_day = record[0]
    current_value = float(record[4])

    deficit = previous_value - current_value
    
    if current_value < previous_value:
        deficits.append({"day": current_day, "amount": deficit})
        print(f"[NET PROFIT DEFICIT] DAY: {current_day}, AMOUNT: SGD{deficit}")
    previous_value = current_value

# Sort the top deficits based on amount (descending order)
def get_deficit_amount(value):
    return value["amount"]
net_profit_deficit = sorted(deficits, key=get_deficit_amount, reverse=True)

highest_deficit = net_profit_deficit[0]
print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {highest_deficit['day']}, AMOUNT: SGD{highest_deficit['amount']}")

# 2nd highest cash deficit
second_deficit = net_profit_deficit[1]
print (f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {second_deficit['day']}, AMOUNT: SGD {second_deficit['amount']}")

# 3rd highest cash deficit
third_deficit = net_profit_deficit[2]
print(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {third_deficit['day']}, AMOUNT: SGD{third_deficit['amount']}")