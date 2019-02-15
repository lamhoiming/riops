#%% Julian day counter modules
# Taken from Enno Middleberg's site of useful astronomical python references: http://www.astro.rub.de/middelberg/python/python.html
# Adopted by Lam Hoi Ming 2019-02-14
def gd2jd(date):
    
    yyyy = int(date[0:4])
    mm = int(date[4:6])
    dd = int(date[6:8])
        
    # Do we have a leap year? 
    daylist=[31,28,31,30,31,30,31,31,30,31,30,31]
    daylist2=[31,29,31,30,31,30,31,31,30,31,30,31]
    if (yyyy%4 != 0):
        days=daylist
    elif (yyyy%400 == 0):
        days=daylist2
    elif (yyyy%100 == 0):
        days=daylist
    else:
        days=daylist2
    
    # Counting from zero (python convention)
    daysum = 0
    for y in range(mm - 1):
        daysum = daysum + days[y]
    ju_day = daysum + dd - 1
    print('year =', yyyy, '.', 'julian day =', ju_day, '.', 'January 1st is set as zero.')

#%% Julian day to yyyyddmm format
# Task to convert a list of julian dates to gregorian dates
# description at http://mathforum.org/library/drmath/view/51907.html
# Original algorithm in Jean Meeus, "Astronomical Formulae for Calculators
# Adopted by Lam Hoi Ming 2019-02-14

def jd2gd(yyyy, ju_day):
    
    #yyyy = int(date[0:4])
    # Do we have a leap year? 
    daylist=[31,28,31,30,31,30,31,31,30,31,30,31]
    daylist2=[31,29,31,30,31,30,31,31,30,31,30,31]
    if (yyyy%4 != 0):
        days=daylist
        assert ju_day <= 365 # A year has 365 days only!
    elif (yyyy%400 == 0):
        days=daylist2
        assert ju_day <= 366 # A leap year has 366 days only!

    elif (yyyy%100 == 0):
        days=daylist
        assert ju_day <= 365 # A year has 365 days only!

    else:
        days=daylist2
        assert ju_day <= 366 # A leap year has 366 days only!

    yyyy = str(yyyy)
    mm = 0
    dd = ju_day
    i = 0
    
    
    for i in range(12) :
        mm = mm + 1
        if dd <= days[i]: 
            break
        elif dd > days[i]:
            dd = dd - days[i]

    dd = f"{dd:02d}"
    mm = f"{mm:02d}"
    
    yyyymmdd = yyyy + mm + dd
    print(yyyymmdd)
    
