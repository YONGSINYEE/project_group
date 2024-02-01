from pathlib import Path
import csv

# create a file path to csv file
file_path = [Path.cwd()/"csv_reports"/"overheads (1).csv"]

# create an empty list for overheads record
overheads = []

# read the csv file
for fp in file_path:
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # append amount into the overheads record
        for row in reader:
            overheads.append([row[0], float(row[1])])

# print overheads after reading all files
# print(overheads)

# Scenario 1
# find out the category with the highest value
highest_value = 0 
highest_category = 0

for category, value in overheads:
    if value > highest_value:
        highest_value = value
        highest_category = category
if highest_category:
    print(f"[HIGHEST OVERHEAD] {highest_category.upper()}: {highest_value}%")
else:
    print("No data found.")
