
def main() : 
    usergame = str(input("Enter choice (rock/paper/scissors):"))
    usergame = is_valid_choice(usergame)
    cpuchoice= get_cpu_choice()
    winner = determine_winner(usergame,cpuchoice)
    print(f"You chose {usergame} and computer chose {cpuchoice}")
    print (f"{winner}")

def is_valid_choice(usergame):
    while usergame != "rock" and usergame != "paper" and usergame != "scissors":
        usergame = str(input("Please enter rock, paper, or scissors: "))
    return usergame

ROCK= 1
PAPER = 2
SCISSORS = 3

def get_cpu_choice():
    import random
    number = random.randint(1,3)
    if number == ROCK:
        return "rock"
    elif number == PAPER:
        return "paper"
    elif number == SCISSORS:
        return "scissors"

def determine_winner(usergame,cpuchoice):
    if usergame == cpuchoice:
        winner = "Tie!"
    elif usergame == "rock":
        if cpuchoice == "scissors":
            winner = "You win!"
        else:
            winner = "Computer wins!"
    elif usergame == "paper":
        if cpuchoice == "rock":
            winner = "You win!"
        else:
            winner = "Computer wins!"
    elif usergame == "scissors":
        if cpuchoice == "paper":
            winner = "You win!"
        else:
            winner = "Computer wins!"
    return winner

main()