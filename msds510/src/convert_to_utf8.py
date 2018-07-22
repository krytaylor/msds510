import sys  # import the library
import csv  # import the csv file

arg_list = sys.argv

def main():
    """calls the function that is to be used in the script"""
    # Using csv library, first 'avengers.csv' is opened to as read mode and reading, decoding as ISO-8859-1
    # each line and writing each line to 'avengers_utf.csv' encoded as 'utf-8' character encoding

    file = arg_list[1]  # file variable takes the argument of the first location, the input.
    modified_file = arg_list[2]  # modified file takes the argument of the second location, the output.

    with open(file, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # reader that reads the file like a dictionary

        with open(modified_file, 'w', encoding='utf-8') as new_file:
            # List that contains the header of the csv file
            fieldnames = ['URL', 'Name/Alias', 'Appearances', 'Current?', 'Gender', 'Probationary Introl',
                          'Full/Reserve Avengers Intro', 'Year', 'Years since joining', 'Honorary', 'Death1', 'Return1',
                          'Death2', 'Return2', 'Death3', 'Return3', 'Death4', 'Return4', 'Death5', 'Return5', 'Notes']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,
                                        delimiter=',')

            csv_writer.writeheader()  # use the writeheader method to write the header rows

            # writing one line at a time in the new csv file
            for line in csv_reader:
                csv_writer.writerow(line)


if __name__ == "__main__":
    main()
