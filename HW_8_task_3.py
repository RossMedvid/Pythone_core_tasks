def shorten_to_date(long_date):
    a=long_date.split(',')
    return a[0]


print(shorten_to_date("Monday February 2, 8pm"))