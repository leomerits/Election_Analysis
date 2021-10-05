# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage og votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datatime class to get the present time.
now = dt.datetime.now()
#Print the present time.
print("The time right now is ", now)

import csv
import os 
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)
# Create a filename variable to a direct or indirect apth to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election resultsand read the file.
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)  

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


