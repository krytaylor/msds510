import csv
import sys

arg_list = sys.argv

filename = arg_list[1]  # fieldnames variable set to argument 1
lines = []

with open(filename, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        lines.append(line)  # Add lines in the list

print('161th record: ', lines[161].values())  # Print the values in the dictionary list
print('161th fieldnames : ', lines[161].keys())  # Print the keys in fieldnames
