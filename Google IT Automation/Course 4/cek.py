import requests
import csv
import datetime


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    
    date_dict = {}
    min_date = datetime.datetime.today()
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        
        if row_date > start_date:
            if row_date not in date_dict.keys():
                date_dict[row_date] = date_dict.get(row_date)
            date_dict[row_date] = [row[0] + " " + row[1]]
        
    print(date_dict)    

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

start_date = get_start_date()
get_same_or_newer(start_date)
