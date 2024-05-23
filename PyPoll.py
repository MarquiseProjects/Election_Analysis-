# Add our dependencies.
import csv
import os

# Create a path to Resources folder 
resources_path = "/Users/apple/Desktop/Election_Analysis/Resources"
# Assign a variable to load a file from a path.
file_to_load = os.path.join(resources_path, "election_results.csv")
# Create a path to analysis folder 
desktop_path = "/Users/apple/Desktop"
analysis_path = os.path.join(desktop_path, "analysis")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(analysis_path, "election_analysis.txt")


#Vote counter variable 
total_votes = 0
#Declare a new list 
candidate_options = []
#Create an empty dictionary 
candidate_votes = {}
# Winning Candidate and Winning Count Tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count 
        total_votes += 1

        #  Print the candidate name from each row 
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # Add the cadidate name to the list 
            candidate_options.append(candidate_name)

            # Begin tracking that candidae's vote count. 
            candidate_votes[candidate_name] = 0 

         # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1 

# Print the candidate list.
#print(candidate_options)

#Print the candidate vote dictionary 
#print(candidate_votes)

# DETERMINE THE PERCENTAGE OF VOTES PER CANDIDATE 
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
  # 2. Retrive vote count of a candiate. 
  votes = candidate_votes[candidate_name]
  # 3. Calculate the percentage 
  vote_percentage = float(votes) / float(total_votes) * 100
  # 4. Print the candiate name and percentage of votes.
  #print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")
  
  #Determine if the vote count and candidate 

  # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
  print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

  #1. Determine if the votes is greater than the winning count. 
  if (votes > winning_count) and (vote_percentage > winning_percentage):
      
      # 2. If ture then set winning_count = votes and winning_percent = vote_percentage. 
      winning_count = votes
      winning_percentage = vote_percentage

      # 3. Set the winning_candidate equal to the candidate's name.
      winning_candidate = candidate_name 
  

      winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)