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

# Initialize a total vote count.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning candidate and Winning Count Tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)  

    # Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the vote count
        total_votes += 1

        # Print the candidates name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate,
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes foe each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # To Do: Print out each candidate's name, vote count, and percentage of votes to the terminal.
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percentage = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            
        winning_candidate_summary = (
            f"--------------------------\n"
            f"winner: {winning_candidate}\n"
            f"winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------------\n")
        print(winning_candidate_summary)




