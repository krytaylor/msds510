import msds510.util as mod
import sys
import csv

arg_list = sys.argv

file = arg_list[1]
modified_file = arg_list[2]


# lines variable set to read each line in the file

"""defines the function"""
def main():
    with open(file, 'r', newline='') as csv_file:
        lines = csv_file.readlines()



        # add the month joined to the fields
        fields = mod.line_to_row(lines[0])
        nice_fields = mod.line_to_row(
            mod.make_nice_name(lines[0]))
        nice_fields.append('month_joined')  

        # open modfied and processed file in write mode
        lines.remove(lines[0])
        with open(modified_file, 'w', encoding='utf-8') as new_file:


            # write like a dictionary with the new file, fieldnames set to nice fields and with delimiter
            csv_writer = csv.DictWriter(new_file, fieldnames=nice_fields,
                                        delimiter=',')
            csv_writer.writeheader()

            # writing one line at a time in the new csv file
            for line in lines:
                row = mod.line_to_row(line)
                record = mod.row_to_record(row, nice_fields)

                # the new file record is transformed record in the dictionary for each record
                transformed_record = mod.transform_record(
                    record)

                # use the row writer method to write the transformed record for each row
                # new record month joined is changed
                transformed_record['month_joined'] = mod.get_month(
                    str(transformed_record['full_reserve_avengers_intro']))
                csv_writer.writerow(
                    transformed_record)


if __name__ == '__main__':
    main()
