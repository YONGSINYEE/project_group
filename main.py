from pathlib import Path
import overheads
import cash_on_hand
import profit_and_loss 

# Create and write a txt file. Name it as "summary_report.txt"
file_path = Path.cwd() / "summary_report.txt"
with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
    # First Scenario 
    # Each value on current day is higher than the previous day in cashonhand and profit and loss
    # Print the output with the required format
    # HIGHEST OVERHEADS
    file.write(f"[HIGHEST OVERHEAD] {overheads.highest_category.upper()}: {overheads.highest_value}%\n")
    # CASH SURPLUS 
    file.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
    file.write(f"[HIGHEST CASH SURPLUS] DAY: {cash_on_hand.highest_surplus_day}, AMOUNT: SGD{int(cash_on_hand.highest_surplus)}\n")
    # NET PROFIT SURPLUS
    file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
    file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {profit_and_loss.highest_surplus_day}, AMOUNT: SGD{int(profit_and_loss.highest_surplus)}\n")

    # Second Scenario
    # Each value on current day is lower than the previous day in cashonhand and profit and loss
    # HIGHEST OVERHEADS
    file.write(f"\n[HIGHEST OVERHEAD] {overheads.highest_category.upper()}: {overheads.highest_value}%\n")
    # CASH DEFICIT
    file.write(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
    file.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_on_hand.highest_deficit_day}, AMOUNT: SGD{int(cash_on_hand.highest_cash_deficit)}\n")
    # NET PROFIT DEFICIT 
    file.write(f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
    file.write(f"[HIGHEST PROFIT DEFICIT] DAY {profit_and_loss.highest_deficit_day}, AMOUNT: SGD{int(profit_and_loss.highest_netprofit_deficit)}\n")

    # Third Scenario
    # Top3 value can be higher or lower than the previous day in cashonhand and profit and loss
    # OVERHEADS
    file.write(f"\n[HIGHEST OVERHEAD] {overheads.highest_category.upper()}: {overheads.highest_value}%\n")
    # TOP 3 CASH DEFICITS
    for deficit in cash_on_hand.deficits:
        file.write(f"[CASH DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{int(deficit['amount'])}\n")

    file.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_on_hand.highest_deficit['day']}, AMOUNT: SGD{int(cash_on_hand.highest_deficit['amount'])}\n")
    file.write(f"[2ND HIGHEST CASH DEFICIT] DAY: {cash_on_hand.second_deficit['day']}, AMOUNT: SGD {int(cash_on_hand.second_deficit['amount'])}\n")
    file.write(f"[3RD HIGHEST CASH DEFICIT] DAY: {cash_on_hand.third_deficit['day']}, AMOUNT: SGD{int(cash_on_hand.third_deficit['amount'])}\n")

    # TOP 3 NET PROFIT DEFICITS
    for deficit in profit_and_loss.deficits:
        file.write(f"[NET PROFIT DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{int(deficit['amount'])}\n")

    file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss.highest_deficit['day']}, AMOUNT: SGD{int(profit_and_loss.highest_deficit['amount'])}\n")
    file.write(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss.second_deficit['day']}, AMOUNT: SGD {int(profit_and_loss.second_deficit['amount'])}\n")
    file.write(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss.third_deficit['day']}, AMOUNT: SGD{int(profit_and_loss.third_deficit['amount'])}\n")