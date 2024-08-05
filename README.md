# python_challenge

##Overview
This repository contains two Python projects: PyBank and PyPoll. Each project analyzes CSV data to provide meaningful insights.

###PyBank
PyBank is designed to analyze financial data. It calculates the total number of months included in the dataset, the net total amount of "Profit/Losses" over the entire period, and the average change in "Profit/Losses" during the period. Additionally, it identifies the greatest increase and decrease in profits over the entire period.

To use PyBank, place the financial_data.csv file in the PyBank directory. Then, run the pybank.py script. The script will process the data and save the analysis report as financial_analysis.txt in the analysis folder within the PyBank directory.

###PyPoll
PyPoll is designed to analyze election data. It calculates the total number of votes cast, provides a list of candidates who received votes, calculates the percentage of votes each candidate won, and the total number of votes each candidate received. Finally, it determines the winner of the election based on the popular vote.

To use PyPoll, place the election_data.csv file in the PyPoll directory. Then, run the pypoll.py script. The script will process the data and save the election results report as election_results.txt in the analysis folder within the PyPoll directory.

##Directory Structure
The repository has the following structure:

The python_challenge directory contains two subdirectories, PyBank and PyPoll. Each subdirectory contains the respective CSV file (financial_data.csv for PyBank and election_data.csv for PyPoll), the Python script (pybank.py for PyBank and pypoll.py for PyPoll), and an analysis folder where the output text files are saved (financial_analysis.txt for PyBank and election_results.txt for PyPoll).
