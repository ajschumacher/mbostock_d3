__author__ = 'Kevin Chang'

import json


# Instantiate Globals
list_of_dayofweek_commits = {}
temp_count = 0


# Input file designation
input_file = ".\mbostock_d3_punch_card.txt"


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
    max_commit_count = max(list_of_dayofweek_commits.values())
    keys = [a for a, b in list_of_dayofweek_commits.items() if b == max_commit_count]

    if keys[0] == 0:
        dayofweek = "Sunday"
    if keys[0] == 1:
        dayofweek = "Monday"
    if keys[0] == 2:
        dayofweek = "Tuesday"
    if keys[0] == 3:
        dayofweek = "Wednesday"
    if keys[0] == 4:
        dayofweek = "Thursday"
    if keys[0] == 5:
        dayofweek = "Friday"
    if keys[0] == 6:
        dayofweek = "Saturday"

    print "In the last year, the greatest number of commits were issued on " + dayofweek + "'s with " \
          + str(max_commit_count) + " commits."

    data_file.close()








