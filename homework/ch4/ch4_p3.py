keepgoing = "y"
while keepgoing != "n":
    userenter = int(input("Enter a number: ")) #ask user to enter a number
    reverseddigit = 0
    while userenter != 0:
        digit = userenter % 10
        reverseddigit = reverseddigit  * 10 + digit
        userenter //= 10
    print("Reversed Number: " + str(reverseddigit))
    keepgoing = input("Again?: ")
else:
    print ("Goodbye!")
