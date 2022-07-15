import random

def rockpaperscissors():
    print ("Let's play rock paper scissors")
    decisionList = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(decisionList)
    userChoice = input("Choose rock (r), paper(p) or scissors (s) :")
    print("The computer chooses " +computerChoice)
    if (userChoice == 'r' and computerChoice == "scissors") or (userChoice == 'p' and computerChoice == "rock") or (userChoice == 's' and computerChoice == "paper"):
        print("you win :)")
    elif (userChoice == 'r' and computerChoice == 'rock') or (userChoice == 'p' and computerChoice == 'paper') or (userChoice == 's' and computerChoice == 'scissors'):
        print("it's a draw")
    elif (userChoice == 'r' and computerChoice == 'paper') or (userChoice == 'p' and computerChoice == 'scissors') or (userChoice == 's' and computerChoice == 'rock'):
        print("you lose :(")

rockpaperscissors()