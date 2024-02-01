from pathlib import Path
import overheads
import cash_on_hand
import profit_and_loss 

file_path = Path.cwd() / "summary_report.txt"
with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
    # First Scenario
    file.write("First Scenario:\n")
    file.write(f"[HIGHEST OVERHEAD] {overheads.highest_category.upper()}: {overheads.highest_value}%\n")
    file.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
    file.write(f"[HIGHEST CASH SURPLUS] DAY: {cash_on_hand.highest_surplus_day}, AMOUNT: SGD{cash_on_hand.highest_surplus}\n")
    file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
    file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {profit_and_loss.highest_surplus_day}, AMOUNT: SGD{profit_and_loss.highest_surplus}\n")

    # Second Scenario
    file.write(f"\n[HIGHEST OVERHEAD] {overheads.highest_category.upper()}: {overheads.highest_value}%\n")
    file.write(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
    file.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_on_hand.highest_deficit_day}, AMOUNT: SGD{cash_on_hand.highest_cash_deficit}\n")
    file.write(f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
    file.write(f"[HIGHEST PROFIT DEFICIT] DAY {profit_and_loss.highest_deficit_day}, AMOUNT: SGD{profit_and_loss.highest_deficit}\n")

    # Third Scenario
    file.write(f"\n[HIGHEST OVERHEAD] {overheads.highest_category.upper()}: {overheads.highest_value}%\n")
    for deficit in cash_on_hand.deficits:
        file.write(f"[CASH DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{deficit['amount']}\n")

    file.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_on_hand.highest_deficit['day']}, AMOUNT: SGD{cash_on_hand.highest_deficit['amount']}\n")
    file.write(f"[2ND HIGHEST CASH DEFICIT] DAY: {cash_on_hand.second_deficit['day']}, AMOUNT: SGD {cash_on_hand.second_deficit['amount']}\n")
    file.write(f"[3RD HIGHEST CASH DEFICIT] DAY: {cash_on_hand.third_deficit['day']}, AMOUNT: SGD{cash_on_hand.third_deficit['amount']}\n")

    # Detailed net profit deficits
    for deficit in profit_and_loss.deficits:
        file.write(f"[NET PROFIT DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{deficit['amount']}\n")

    file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss.highest_deficit['day']}, AMOUNT: SGD{profit_and_loss.highest_deficit['amount']}\n")
    file.write(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss.second_deficit['day']}, AMOUNT: SGD {profit_and_loss.second_deficit['amount']}\n")
    file.write(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss.third_deficit['day']}, AMOUNT: SGD{profit_and_loss.third_deficit['amount']}\n")
