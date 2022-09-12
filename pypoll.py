'''


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#open the election results and read the file

with open(file_to_load) as election_data:

#To do: perform analysis.

    print(election_data)


#Close the file
'''
import os
import csv

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}



with open(file_to_load) as election_data:
    # Read and analyze the data here
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)


    for row in file_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    # Winning Candidate and Winning Couunt tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/ float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage}% of the vote")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate,}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n"
    )
    
    print(winning_candidate_summary)

print(total_votes)
print(candidate_options)
print(candidate_votes)

'''
with open(file_to_save, "w") as txt_file:

    #three counties to the file
    txt_file.write("Counties in the Election \n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")

'''