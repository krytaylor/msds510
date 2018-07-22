import msds510.util as mod
import csv
import sys

#implement the msds510 folder as utility as a module to use to run script

arg_list = sys.argv

#fieldname variable takes the argument list 1

filename = arg_list[1]

lines = []

#use reader as a dictionary which is how the lines will be formatted
with open(filename,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #for each line in reader, add line to the name lines
    for line in csv_reader:
        lines.append(line)

            #the conditions to print the content of the record
        print('Input Record - {\'year\':' +line['year']+', \'intro\': '+line['full_reserve_avengers_intro']+'}')
        print('Date joined - '+str(mod.get_date_joined(str(line['year']),str(line['full_reserve_avengers_intro']))))
        print('Days since joined - '+str(mod.days_since_joined(str(line['year']),str(line['full_reserve_avengers_intro']))))


        print()
        print()

