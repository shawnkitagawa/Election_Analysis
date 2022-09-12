
from datetime import datetime
import csv

now = datetime.now()
print("The time right now is " , now)
print(dir(datetime))

'''

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

for i in voting_data:
    county = i["county"]

'''
'''
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for keys, values  in counties_dict.items():
    print(f"{keys} country has {values} refistered voters.")

'''
'''
voting_data = [
{"county":"Arapahoe", "registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}
 ]





for i in voting_data:
    County = i["county"]
    Registered_voters = i["registered_voters"]
    print(f"{County} country has {Registered_voters} refistered voters.")
'''