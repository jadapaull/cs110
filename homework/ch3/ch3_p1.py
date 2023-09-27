#User enters a number 1-7
userenter=int(input("Enter an integer in the range 1-7: ")) 
if userenter == 1: # if equal to 1 print sunday
    print ("Sunday is the first day of the week.")
elif userenter == 2:    #if equal to 2 print monday
    print ("Monday is the second day of the week.")
elif userenter == 3:    #if equal to 3 print tuesday
    print ("Tuesday is the third day of the week.")
elif userenter == 4:    #if equal to 4 print wednesday
    print("Wednesday is the fourth day of the week.")
elif userenter == 5:    #if equal to 5 print thursday
    print ("Thursday is the fifth day of the week.")
elif userenter == 6:    #if equal to 6 print friday
    print("Friday is the sixth day of the week.")
elif userenter == 7:    # if equal to 7 print saturday
    print("Saturday is the seventh day of the week.")
else:       # if any other integer is entered print this
    print("Invalid integer entered. Please Try Again")