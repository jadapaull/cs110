wordone=str(input("Enter word #1: "))   #user enters word one
wordtwo= str(input("Enter word #2: "))  #user enters word two
wordthree= str(input("Enter word #3: "))   #user enters word three

print("Alphabetical order: ", end="")   #prints alphabetical order and does not create a new line

if wordone < wordtwo and wordone < wordthree:       #trying to find less than 
    print ( wordone, end=", ")    #end without starting a new line and inputing a comma and space
elif wordtwo < wordone and wordtwo < wordthree:     #trying to find less than 
    print(wordtwo,end=", ")      #end without starting a new line and inputing a comma and space
elif wordthree < wordone and wordthree < wordtwo:   #trying to find less than 
    print(wordthree, end=", ")   #end without starting a new line and inputing a comma and space

if wordtwo > wordone and wordtwo < wordthree:           #trying to find the middle number
    print(wordtwo, end=", ")        #end without starting a new line and inputing a comma and space
elif wordone > wordtwo and wordone < wordthree:         #trying to find the middle number
    print ( wordone, end=", ")       #end without starting a new line and inputing a comma and space
elif wordthree > wordtwo and wordthree < wordone:      #trying to find the middle number
    print(wordthree, end=", ")       #end without starting a new line and inputing a comma and space
elif wordtwo < wordone and wordtwo > wordthree:         #trying to find the middle number
    print(wordtwo, end=", ")         #end without starting a new line and inputing a comma and space
elif wordone < wordtwo and wordone > wordthree:         #trying to find the middle number
    print (wordone, end=", ")        #end without starting a new line and inputing a comma and space
elif wordthree < wordtwo and wordthree > wordone:       #trying to find the middle number
    print(wordthree, end=", ")       #end without starting a new line and inputing a comma and space

if wordtwo >wordone and wordtwo > wordthree:        #trying to find the last or greatest number
    print(wordtwo)          #printing the result of if statement 
elif wordone > wordtwo and wordone > wordthree:     #trying to find the last or greatest number
    print(wordone)          #printing the result of if statement 
elif wordthree > wordone and wordthree > wordtwo:   #trying to find the last or greatest number
    print(wordthree)        #printing the result of if statement 