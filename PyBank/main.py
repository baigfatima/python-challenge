import csv

file_to_load = "raw_data/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
total_profit = 0

with open(file_to_load) as profit_data:
    reader = csv.DictReader(profit_data)

    for row in reader:

        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit_Losses"])

        profit_change = int(row["Profit_Losses"]) - prev_profit
        prev_profit = int(row["Revenue"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = month_of_change + [row["Date"]]

        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profit_change

        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profit_change

    profit_avg = sum(profit_change_list) / len(profit_change_list)

    output = (
        f"\nFinancial Analysis\n"
        f"------------------------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total Profit_Losses: ${total_profit}\n"
        f"Average Profit Change: ${profit_avg}\n"
        f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

    print(output)

    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)

