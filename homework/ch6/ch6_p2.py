import random

def main():
    file = open('Desktop/random_ints.txt', 'w')
    integer = valid()
    while type(integer) != int:
        integer = valid(integer)
    integer = int(integer)
    randWrite(integer, file)
    file.close()

def randWrite(num, file):
    i = 0
    while i + 1 < num:
        number = str(random.randint(1, 100))
        file.write(number)
        file.write('\n')
        i += 1
    number = str(random.randint(1, 100))
    file.write(number)

def valid():
    integer = input("Please enter an integer: ")
    try:
        integer = int(integer)
    except:
        print("Not a valid integer.")
        integer = valid()
    return integer

main()
