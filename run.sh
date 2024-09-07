#!/bin/bash

# Define the time limit in days, hours, minutes, and seconds
days=0
hours=0
minutes=1
seconds=0

# Convert everything to seconds
time_limit=$((days*86400 + hours*3600 + minutes*60 + seconds))

nohup python3 -u generate.py $time_limit >> res.txt &
