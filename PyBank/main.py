import os
import csv

file = 'Resources/budget_data.csv'

# Read the CSV file
def load_data(filename):
    with open(filename, mode='r') as filename:
        reader = csv.reader(filename)
        header = next(reader)
        data = [(row[0], int(row[1])) for row in reader]

        return data

budget = load_data(file)

total_months = len(budget)

net_total = sum([record[1] for record in budget])

changes=[]
for i in range(0, len(budget)-1):
    change = budget[i+1][1] - budget[i][1]
    changes.append(change)

average=(sum(changes)/len(changes))

minimum= (min(changes))
min_position=(changes.index(minimum)+1)
min_month=(budget.pop(min_position)[0])

maximum= (max(changes))
max_position=(changes.index(maximum))
max_month=(budget.pop(max_position)[0])

analysis_report = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average:.2f}\n"
    f"Greatest Increase in Profits: {max_month} (${maximum})\n"
    f"Greatest Decrease in Profits: {min_month} (${minimum})\n"
)

print(analysis_report)

output_dir = '/Users/juansegovia/Desktop/Classwork Projects/python_challenge/PyBank/analysis'

output_path = os.path.join(output_dir, 'financial_analysis.txt')

# Write the analysis to the text file
with open(output_path, mode='w') as file:
    file.write(analysis_report)

