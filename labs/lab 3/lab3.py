import random

def main():
    exitinput = ''
    rounds = 0
    correct = 0
    while exitinput != 'exit':
        rounds += 1
        binarynum = generatebinary()
        userguess =int(input(f"What is the decimal number of the binary number {binarynum}? "))
        check = checkbinary(binarynum, userguess)
        if check == True: 
            correct += 1
            print ("Correct!")
        else: 
            print("Incorrect!")
        exitinput =str(input("Enter 'exit' to quit. Enter anything else to play again. "))
    else: 
        print(f"In {rounds} round(s) you answered {correct} questions correctly")

def generatebinary():
    binarynum ="" 
    for i in range(5):
        rand =str(random.randint(0,1))
        binarynum += rand 
    return binarynum

def checkbinary(binarynum, userguess):
    squared = len(binarynum) - 1
    decimalnum = 0
    for i in binarynum: 
        value = 2 ** squared 
        squared -= 1
        if i == "0":
            value = 0 
        decimalnum += value
    return decimalnum == userguess
    
            




main()