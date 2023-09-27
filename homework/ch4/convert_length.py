YARD_INCHES = 36
YARD_FEET = 3
FOOT_INCHES = 12

userinput = int(input("Enter a number of inches: "))
yards = userinput // YARD_INCHES
feet = int(userinput / FOOT_INCHES % YARD_FEET)
inches = userinput % FOOT_INCHES

yardtense = ''
foottense = 'foot'
inchtense = ''
if yards != 1:
    yardtense = 's'
if feet != 1:
    foottense = 'feet'
if inches != 1:
    inchtense = 'es'
print(f"{userinput} inches is {yards} yard{yardtense}, {feet} {foottense}, and {inches} inch{inchtense}.")