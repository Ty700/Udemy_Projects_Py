def is_leap(year):
    """Given a year, will determine if it's a leap year"""
    if(year % 4 != 0):
        return False
    elif(year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

def days_in_month(year, month):
    monthDaysForNonLeapYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(is_leap(year) and month == 2):
        return 29
    else:
        return monthDaysForNonLeapYear[month - 1]

def get_month_name(monthNumber):
    """Takes a month number and returns the month name. I.E: 6 will return "June" """ #DOCSTRING
    monthNames = {
        1: "January",
        2: "Feburary",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    return(monthNames[monthNumber])

def main():
    year = int(input("Enter in a year: "))
    month = int(input("Enter in the month's number. Example: June = 6, Jan = 1 "))
    days = days_in_month(year, month)
    
    print(f"{get_month_name(month)} in {year} has {days} days")

if __name__ == "__main__":
    main()
