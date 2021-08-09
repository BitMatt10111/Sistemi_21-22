'''
Name: Matteo Lamberti
Data: 28/07/21

Given a moment, determine the moment that would be after a gigasecond has passed.
A gigasecond is 10^9 (1,000,000,000) seconds.
'''

from datetime import datetime,timedelta
gigasecond=1000000000

def main():
    while True:
        is_valid=True
        input_date = input("Enter the date in format 'dd/mm/yy' : ")
        date_list=input_date.split("/")
        try:
            date=datetime(int(date_list[2]),int(date_list[1]),int(date_list[0]))
        except:
            is_valid=False
        if is_valid==True:
            break
    end_date = date + timedelta(seconds=gigasecond)
    print(end_date)

if "__main__"==__name__:
    main()