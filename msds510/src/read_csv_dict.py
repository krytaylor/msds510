import csv
import sys

arg_list = sys.argv

# fieldnames variable set to argument 1
filename = arg_list[1]
lines = []

# Add lines in the list
with open(filename, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        lines.append(line)
# Print the values in the dictionary list
print('161th record: ', lines[161].values())
print('161th fieldnames : ', lines[161].keys())
