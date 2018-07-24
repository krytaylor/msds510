import datetime
import calendar

"""calls the function that is to be used in the script
 returns the days since joined
 """
"""
    Module: util

    This is container for the helper functions.

    Functions:
    1. get_month
    2. get_month
    3. get_date_joined
    4. days_since_joined
    5. line_to_row
    6. row_to_record
    7. make_nice_name
    8. transform_record

"""
def main():
    print(days_since_joined('2013', '13-Nov'))

"""
    Do extract the month from a date

    Returns : datetime

    Input arguments: datetime

"""

def get_month(date):

    if len(date) == 0 or date == 'YES':
        return
    date = date.split('-')

    month = date[1] if date[0].isdigit() else date[0]

    return datetime.datetime.strptime(month,'%b').month


 """
    Do returns date a particular character joining the avenger

    Returns : datetime

    Input arguments: int , datetime

    """
def get_date_joined(year,day):
    date = day.split('-')

    # year is set to integer year
    year = int(year)
    month = get_month(day)

    # get day number if same as header row or else the second row
    day = int(date[0] if date[0].isdigit() else date[1])%calendar.monthrange(year,month)[1]
    return datetime.date(year,month,day)


"""
    Do returns number of days since a particular character joined the avenger

    Returns : datetime

    Input arguments: int , datetime

    """
def days_since_joined(year,day):
    today = datetime.date.today()

    #subtract date joined year and day by today's date
    return today - get_date_joined(year,day)

"""
    Do convert a line from csv file to a row list

    Returns : str

    Input arguments: list

    """
def line_to_row(line):
    return line.split(',')

"""
    Do convert a row and it's fields to a record

    Returns : dictionary

    Input arguments: list, list
    """

def row_to_record(row,fields):

     return dict(zip(fields,row))

"""
    Do make a name prettier by eliminating  unwanted characters

    Returns : str

    Input arguments: str

    """
#In the name, replace the spaces with underscore, the slashes with underscore and make lowercase
def make_nice_name(name):
    return name.replace(' ','_').replace('/','_').lower().strip()

"""
    Do transform dictionary 
    
    Returns : new record dictionary
    
    Input arguments: record dictionary
    
     """
def transform_record(record_dict):

    #read transformed record as dictionary
    record_dict['notes'] = record_dict['notes'].strip()
    for key, value in record_dict.items():
        if key == 'death' or key == 'return':
            record_dict[key] = to_bool(record_dict[key])
    return record_dict

if __name__ == "__main__":
    # execute only if run as a script
    main()
