import csv
import sys

arg_list = sys.argv

filename = arg_list[1]  # fieldname variable is eqal to first arugment
lines = []  # lines are a list

# The new 'avengers_utf.csv' file is then opened again as read mode
with open(filename, 'r') as csv_file:
    # each line from the file is read and added to a list named 'lines'
    for line in csv_file:
        lines.append(line)  # for each line add the line to lines that is read

# Printing the number of rows in lines list indexed at 161
print('162nd Row: ', lines[161])
