#!/usr/bin/env bash

# example of the run script for running the word count

# first I'll load all my dependencies
# no dependencies used

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./weekcommits.py
chmod a+x ./dayofweek.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python ./weekcommits.py
python ./dayofweek.py

