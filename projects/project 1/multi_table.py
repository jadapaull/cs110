def main():
    usertable = user_table()
    make_table(usertable)
    playagain = play_again()
    if playagain == 'y':
        main()
    else:
        print("Goodbye!")
        return

def user_table():
    usertable= int(input("Enter a number (2-20):"))

    while usertable < 2 or usertable > 20 :
        usertable= int(input("Please enter an integer between 2 and 20:"))
    return usertable

def make_table(usertable):
    for column in range (1, usertable+1):
        print("\t", column, end='')
    print("\tRow Total")

    for row in range(1,usertable+1):
        sum = 0
        print(row, end='')
        for col in range(1,usertable+1):
            print("\t", row * col, end='')
            sum += col * row
        print("\t", sum)
    return

def play_again():
    playagain = input("Would you like to generate another multiplication table? (y/n): ")
    while playagain != 'y' and playagain != 'n':
        playagain = input("Please enter 'y' for yes and 'n' for no: ")
    return playagain

main()