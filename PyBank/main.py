import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

months_count = 0
total_net = 0
month_of_change = []
budget_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    months_count += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:

        months_count += 1

        total_net += int(row[1])

        budget_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        budget_change_list += [budget_change]
        month_of_change += [row[0]]

        if budget_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = budget_change

        
        if budget_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = budget_change


net_monthly_avg = sum(budget_change_list) / len(budget_change_list)


output = (f"Financial Analysis\n" f"---------------------------------\n" f"Total Months: {months_count}\n" f"Total: ${total_net}\n"
        f"Average Change: ${net_monthly_avg}\n" f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


print(output)

analysis_output = os.path.join("analysis", "results.txt")
with open(analysis_output, "w") as txt_file:
    txt_file.write(output)
     
             




   




    


     

        



         





    

