import datetime


def print_header():
    print("--------------------------------")
    print("		  BIRTHDAY APP")
    print("--------------------------------")


def get_user_birtday():
    year = int(input("What year were you born [YYYY]? "))
    month = int(input("What month were you born [MM]? "))
    day = int(input("What day were you born [DD]? "))

    bday = datetime.date(year, month, day)

    return bday


def count_days_between_dates(bday, today):
    # need to convert bday year to current year
    this_year = datetime.date(year=today.year, month=bday.month, day=bday.day)
    diff_dates = this_year - today

    return diff_dates.days


def print_bday_info(num_days):
    if num_days < 0:
        print("You had your birthday {} days ago this year.".format(-num_days))
    elif num_days > 0:
        print("Your birthday is in {} days!".format(num_days))
    else:
        print("Today is your birthday, congratzzz!")


def main():
    print_header()
    bday = get_user_birtday()
    today = datetime.date.today()
    num_days = count_days_between_dates(bday, today)
    print_bday_info(num_days)

main()