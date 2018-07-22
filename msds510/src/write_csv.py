import sys
import csv

arg_list = sys.argv


# Using csv library, first 'avengers.csv' is opened to as read mode and reading, decoding as ISO-8859-1
# each line and writing each line to 'avengers_utf.csv' encoded as 'utf-8' character encoding

"""calls the names that is to be used in the script"""
def make_nice_name(name):
    return name.replace(' ', '_').replace('/', '_').lower().strip()  # create dictionary that replaces spaces and slashes with underscores, and lowercase

file = arg_list[1]  # file and modified file variables set to the two arguments. The input and output
modified_file = arg_list[2]

with open(file, 'r', newline='') as csv_file:  # opens files in readmode
    csv_reader = csv.DictReader(csv_file)  # the file is read like a dictionary

    with open(modified_file, 'w', encoding='utf-8') as new_file:
        # List that contains the header of the csv file
        fieldnames = fieldnames = ['URL', 'Name/Alias', 'Appearances', 'Current?', 'Gender', 'Probationary Introl',
                                   'Full/Reserve Avengers Intro', 'Year', 'Years since joining', 'Honorary', 'Death1',
                                   'Return1', 'Death2', 'Return2', 'Death3', 'Return3', 'Death4', 'Return4', 'Death5',
                                   'Return5', 'Notes']

        pretty_names = []
        for name in fieldnames:
            pretty_names.append(make_nice_name(name))  # add make_nice_name(value) to the list called pretty_names

        csv_writer = csv.DictWriter(new_file, fieldnames=pretty_names,
                                    delimiter=',')  # Dictionary writer containing new file, fieldnames and delimiter

        csv_writer.writeheader()  # the writer method to write the fieldnames

        # writing one line at a time in the new csv file
        for line in csv_reader:

            keys = []  # keys is the list
            values = line.values()  # values is the value of each line

            for key in line:
                keys.append(
                    make_nice_name(key))  # for each key in the list, add make_nice_name(key) to the dictionary keys

            row = dict(zip(keys, values))  # each row equals to the keys and its values
            csv_writer.writerow(row)  # use writer method to write the row
