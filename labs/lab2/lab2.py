month =int(input( "What is your birth month? (1-12): "))       #asks user for birth month 
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day = int(input("What is the day of your birth? (1-31): "))           #asks user for day of birth, 31 day months
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = int(input("What is the day of your birth? (1-30): "))           #asks user for day of birth, 30 day months
elif month == 2:
    day = int(input("What is the day of your birth? (1-28): "))           #asks user for day of birth, February

if month > 12 or month < 1: 
    print ("invalid birth month. Please try again")         #if the int entered is below 1 or above 12 it prints this

if month == 1 :           #checks for month and prints appropriate sign for month and day
    if day <= 19 and day >=1:           #checks days 
        print("You are a Capricorn!")       
    elif day >=20 and day <= 31:     #checks other "half" of month and assigns appropriate sign
        print ("You are an Aquarius!")
    elif day > 31 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 2:        #checks for days and prints appropriate sign for month and day
    if day <= 18 and day >=1:
        print("You are an Aquarius!")
    elif day >= 19 and day <= 28:        #checks other "half" of month and assigns appropriate sign
        print ("You are a Pisces!")
    elif day > 28 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 3:        #checks for days and prints appropriate sign for month and day
    if day <= 20 and day >=1:
        print("You are a Pisces!")
    elif day >= 12 and day <= 31:        #checks other "half" of month and assigns appropriate sign
        print ("You are an Aries!")
    elif day > 31 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 4:          #checks for days and prints appropriate sign for month and day
    if day <= 19 and day >=1:
        print("You are an Aries!")
    elif day >= 20 and day <= 30:        #checks other "half" of month and assigns appropriate sign
        print ("You are a Taurus!")
    elif day > 30 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 5:           #checks for days and prints appropriate sign for month and day
    if day <= 20 and day >=1:
        print("You are a Taurus!")
    elif day >= 21 and day <= 31:        #checks other "half" of month and assigns appropriate sign
        print ("You are a Gemini!")
    elif day > 31 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 6 :       #checks for days and prints appropriate sign for month and day
    if day <= 20 and day >=1:
        print("You are a Gemini!")
    elif day >= 21 and day <= 30:        #checks other "half" of month and assigns appropriate sign
        print ("You are a Cancer!")
    elif day > 30 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 7:       #checks for days and prints appropriate sign for month and day
    if day <= 22 and day >=1:
        print("You are a Cancer!")
    elif day >= 23 and day <= 31:        #checks other "half" of month and assigns appropriate sign
        print ("You are a Leo!")
    elif day > 31 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 8:       #checks for days and prints appropriate sign for month and day
    if day <= 22 and day >=1: 
        print("You are a Leo!")
    elif day >= 23 and day <= 31:        #checks other "half" of month and assigns appropriate sign
        print ("You are a Virgo!")
    elif day > 31 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 9:       #checks for days and prints appropriate sign for month and day
    if day <= 22 and day >=1 :
        print("You are a Virgo!")
    elif day >= 23 and day <= 30:        #checks other "half" of month and assigns appropriate sign
        print ("You are a Libra!")
    elif day > 30 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 10:      #checks for days and prints appropriate sign for month and day
    if day <= 22 and day >=1 :
        print("You are a Libra!")
    elif day >= 23 and day <= 31:       #checks other "half" of month and assigns appropriate sign
        print ("You are a Scorpio!")
    elif day > 31 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 11:      #checks for days and prints appropriate sign for month and day
    if day <= 21 and day >=1 :
        print("You are a Scorpio!")
    elif day >= 22 and day <= 30:       #checks other "half" of month and assigns appropriate sign
        print ("You are a Sagittarius!")
    elif day > 30 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this

if month == 12:      #checks for days and prints appropriate sign for month and day
    if day <= 21 and day >=1:
        print("You are a Sagittarius!")
    elif day >= 22 and day <= 31:       #checks other "half" of month and assigns appropriate sign
        print ("You are a Capricorn!")
    elif day > 31 or day < 1:
        print ("Invalid day of birth entered.")     #making sure appropriate days of the month if not prints this
