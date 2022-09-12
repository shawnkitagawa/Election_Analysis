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

with open(file_to_load) as election_data:
    # Read and analyze the data here
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)






    '''
with open(file_to_save, "w") as txt_file:

    #three counties to the file
    txt_file.write("Counties in the Election \n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")

'''