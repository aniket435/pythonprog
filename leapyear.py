b=input('enter the number of days in a year')
def leapyear(a):
    if a==366:
        print('the year is leap year')
    elif a==365:
        print('year is not leap year')
    else:
        print('enter a valid days in year')
leapyear(b)