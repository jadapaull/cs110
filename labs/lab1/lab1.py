firstint = int(input("Enter first integer: "))     #user enters first integer
secondint = int(input("Enter second integer: "))    #user enters second integer

addition = firstint + secondint    #finding correct answer for addition
multiplication = firstint * secondint #finding correct answer for multiplication
subtraction= firstint - secondint    #finding correct answer for subtraction
division = firstint / secondint   #finding correct answer for division

firstmath = int(input("what is " + str(firstint) + " + " + str(secondint) + "? "))
#asks user what the sum of the first and second integer is: addition
print(f"Your Answer: {firstmath}") #prints their answer
print (f"Correct Answer: {addition}") #prints the correct answer

secondmath = int(input("what is " + str(firstint) + " - " + str(secondint) + "? "))
#asks user what the difference of the first and second integer is: subtraction
print(f"Your Answer: {secondmath}")  #prints their answer
print (f"Correct Answer: {subtraction}")#prints the correct answer

thirdmath = float(input("what is " + str(firstint) + " / " + str(secondint) + "? "))
#asks user what the quotient of the first and second integer is: division
print(f"Your Answer: {thirdmath}")  #prints their answer
print (f"Correct Answer: {division:.2f}") #prints the correct answer

fourthmath= int(input("what is " + str(firstint) + " * " + str(secondint) + "? "))
#asks user what the product of the first and second integer is : multiplication
print(f"Your Answer: {fourthmath}")  #prints their answer
print (f"Correct Answer: {multiplication}") #prints the correct answer

print("Thanks for playing!")