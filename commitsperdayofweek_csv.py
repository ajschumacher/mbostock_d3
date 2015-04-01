__author__ = 'Kevin Chang'

import json


# Instantiate Globals
list_of_dayofweek_commits = {}
temp_count = 0


# Input file designation
input_file = ".\mbostock_d3_punch_card.txt"
output_file = ".\mbostock_d3_commitsperdayofweek.csv"

# 0-6: Sunday - Saturday
# 0-23: Hour of Day
# Number of Commits
# Parse file to get list of data from json and find max commit day of week & count
with open(input_file) as data_file:
    data = json.load(data_file)
    for day in range(0, 7):
        temp_count = 0
        for value in data:
            if day == value[0]:
                temp_count += value[2]
        list_of_dayofweek_commits[day] = temp_count
    data_file.close()


fileout = open(output_file, "w+")
for dayofweek in range(0, len(list_of_dayofweek_commits)):
    if dayofweek == 0:
        dayofweekstr = "Sunday"
    if dayofweek == 1:
        dayofweekstr = "Monday"
    if dayofweek == 2:
        dayofweekstr = "Tuesday"
    if dayofweek == 3:
        dayofweekstr = "Wednesday"
    if dayofweek == 4:
        dayofweekstr = "Thursday"
    if dayofweek == 5:
        dayofweekstr = "Friday"
    if dayofweek == 6:
        dayofweekstr = "Saturday"
    fileout.write(dayofweekstr + "," + str(list_of_dayofweek_commits[dayofweek]) + "\n")
fileout.close()







