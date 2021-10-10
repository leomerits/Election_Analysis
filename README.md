# Election_Analysis

## Overview of the Election Audit
A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election

1. To calculate the total number of votes cast.
2. To get a complete list of candidates who recieved votes.
3. To calculate the total number of votes each candidate recieved.
4. To calculate the percentage of votes each candidate won.
5. And to determine the winner of the election based on popular vote.

## Resources
- Data Sourcr: election_results.csv
- Software: Python 3.8.8, Visual Studio Code, 1.60.2

## Summary
The analysis of this election audit show that:
- There were 369,711 vote cast in the election

- The Counties results were:
  - Jefferson recieved "10.5%" of the votes and "35.855" number ofvotes.
  - Denver recieved "82.8%" of the votes and "306.055" number f votes.
  - Arapahoe recieved "6.7%" of the votes and "24.801" number of votes.
 
- The county with the largrst turnout of the election:
  - Denver who recieved "82.8%" of the vote and "306.055" number of vote was the county with the largest turnout of the election
  
- The candidates were:
  - Charles Casper Stockham
  - Dianna Degette
  - Raymon Anthony Doane
  
- The candidates results were:
  - Charles Casper Stockham recieved "23.0%" of the votes and "85,213" number of votes. 
  - Dianna Degette recieved "73.8%" of the votes and "272,892" number of votes. 
  - Raymon Anthony Doane recieved "3.1%" of the votes and "11,606" number of votes.
  
- The winner of the election was:
  - Dianna Degette who recieved "73.8%" of the vote and "272,892" number of votes

## Challenge Overview
The overview of this challenge is for us to understand how to use programing tichniques to solve real world events like with did in this State of Colorado congressional election. Without the programing languages and techniques, it would have been much difficult to read throug the csv files to know the actual votes each candidate had, the voter turnout for each county, the percentage of votes from each county out of the total count as well as the county with the highest turnout. With succesfully completing this challenge, the board of election were able to see the txt printed result of the election!

[Election_Results_txt](https://user-images.githubusercontent.com/34757498/136705315-3dadeace-59d1-4ec7-b5b8-3e9eea88a480.png)

## Challenge Summary
With the completion of this audit, I am proud to let the commission know that they are able to use the audit to figure out:
- The Candidates summary results and the candidate that won the elctions with percatage and vote counts.
- The county summary results and the county with the largest turnout which I was able to achieve with the modified script I made, using (votes = county_votes.get(county_name)) to figure out the number of votes each county recieved during the election. Using the if statement, (if (votes > winning_count) and (vote_percentage > winning_percentage):, I was able to get the winning county votes, determing the largest county and percentage vote and finally, was able to print the outcome result to the terminal as well as writing it to a text file for future use.


