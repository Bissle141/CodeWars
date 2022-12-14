# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
    
def which_quarter():  
    '''Will take in a number for the month, and determine what quarter of the year that month is in, then print a line detailing the result and return 1, 2, 3, or 4 depending on what quarter the month was in.'''

    months = "January,February,March,April,May,June,July,August,September,October,November,December"
    month_list = months.split(',')
    
    valid = False
    
    while valid == False:
        month = input("Please input a month, in the form of a number (1-12): \n")
        
        if month.isdigit():
            month = int(month)
            if month > 0 and month <= 12:
                valid = True
            else:
                print("Please input a valid number. \n")
            
        else:
            print("Please input a valid number. \n")
    
    if month <= 3:
        print(f"{month_list[month-1]} is in the first quarter of the year.")
        return 1
    elif month <= 6:
        print(f"{month_list[month-1]} is in the second quarter of the year.")
        return 2
    elif month <= 9:
        print(f"{month_list[month-1]} is in the third quarter of the year.")
        return 3
    else:
        print(f"{month_list[month-1]} is in the fouth quarter of the year.")
        return 4
    
    
which_quarter()