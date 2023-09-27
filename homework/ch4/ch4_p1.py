item = 1
uservalue =int(input("Enter a positive integer: ")) # prompts user to enter a positive integer, converts to integer
for num in range(1, uservalue+1, 1): # tells computer start and end and does not leave out uservalue
    item *= num # Multiplies by next number in range

# Creates string that includes whole numbers from 1 to uservalue, putting x in between each number
plist = ''
for num in range(1, uservalue, 1):
    plist += str(num) # Adds most recent num in range to plist
    plist += " x " # Adds x after num
plist += str(uservalue) # Adds usevalue after last x

print(f"{uservalue}! =", plist, "=", item)