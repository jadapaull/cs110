usernumber1 = int(input("Enter first integer: "))   #this program asks the person for two integers
usernumber2 = int(input("Enter second integer: "))
if usernumber1 > usernumber2:
    mycalculation = usernumber1-usernumber2 * (usernumber1//usernumber2)    #finding my calculation
    modoperator = usernumber1%usernumber2     # finding the correct remainder
    print (f"My calculation : {usernumber1} % {usernumber2} = {mycalculation}") #writing the sentence
    print(f"Mod Operator caluculation: {usernumber1} % {usernumber2} = {modoperator}") #writing the mod operator sentence
else:
    mycalculation = usernumber2-usernumber1 * (usernumber2//usernumber1)    #finding my calculation
    modoperator = usernumber2%usernumber1     # finding the correct remainder
    print (f"My calculation : {usernumber2} % {usernumber1} = {mycalculation}") #writing the sentence
    print(f"Mod Operator caluculation: {usernumber2} % {usernumber1} = {modoperator}") #writing the mod operator sentence


