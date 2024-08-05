import os
import csv

file = 'Resources/election_data.csv'

# Read the CSV file
def load_data(filename):
    with open(filename, mode='r') as filename:
        reader = csv.reader(filename)
        header = next(reader)
        data = [row for row in reader]

        return header, data

header, election = load_data(file)

# print(election)

total_votes= len(election)

candidate_votes = {}

for row in election:
    candidate = row[2]
    if candidate in candidate_votes: # check if the person is in the dictionary
        candidate_votes[candidate] += 1 # if yes, add 1 to their votes
    else:
        candidate_votes[candidate] = 1 # if no, add them to the dictionary and give them 1 vote to start

winner = max(candidate_votes, key=candidate_votes.get)


charles_pct=(candidate_votes["Charles Casper Stockham"]/ total_votes) * 100

diana_pct=(candidate_votes["Diana DeGette"]/ total_votes) * 100
   
ray_pct=(candidate_votes["Raymon Anthony Doane"]/ total_votes) * 100



analysis_report = (
    "Election Results\n"
    "----------------------------\n"
    f"Total Votes: {total_votes}\n"
    "----------------------------\n"
    f"Charles Casper Stockham: {charles_pct:.3f}% ({candidate_votes["Charles Casper Stockham"]})\n"
    f"Diana DeGette: {diana_pct:.3f}% ({candidate_votes["Diana DeGette"]})\n"
    f"Raymon Anthony Doane: {ray_pct:.3f}% ({candidate_votes["Raymon Anthony Doane"]})\n"
    "----------------------------\n"
    f"Winner: {winner}\n"
    "----------------------------\n"
)
print(analysis_report)

output_dir = '/Users/juansegovia/Desktop/Classwork Projects/python_challenge/PyPoll/analysis'

output_path = os.path.join(output_dir, 'election_analysis.txt')

# Write the analysis to the text file
with open(output_path, mode='w') as file:
    file.write(analysis_report)