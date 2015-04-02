__author__ = 'Kevin Chang'

import datetime
import json


# Instantiate Globals
list_of_commits = {}
list_of_max_commits = {}
date_str = ""


# Input file designation
input_file = "mbostock_d3_commit_activity.txt"

# Parse file to get list of data from json and find max commit date & count
with open(input_file) as data_file:
    data = json.load(data_file)
    for list_of_commit_data in data:
        timestamp = list_of_commit_data["week"]
        value = datetime.datetime.fromtimestamp(timestamp).strftime('%m-%d-%Y')
        num_commits = list_of_commit_data["total"]
        list_of_commits[value] = num_commits
        max_commit_count = max(list_of_commits.values())
        keys = [a for a, b in list_of_commits.items() if b == max_commit_count]

    for step in range(0, len(keys)):
        list_of_max_commits[step] = keys[step]
        if step == 0:
            date_str = list_of_max_commits[0]
        if step > 1:
            date_str += " and " + list_of_max_commits[step]

    print "In the last year, the greatest number of commits were issued during the week of " + date_str + " with " + str(max_commit_count) + " commits."

    data_file.close()





