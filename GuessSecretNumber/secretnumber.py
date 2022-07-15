from random import randint,random

def guessNumber(x):
    print('Lets Guess The Secret Number Game!!!')
    secretNum = randint(1,x)
    userNum = '0'
    while secretNum is not userNum:
        userNum = input(f'Choose a number between 1 to {x}: ')
        try:
            if int(userNum) < secretNum:
                print('More!')
            elif int(userNum) > secretNum:
                print('Less!')
            else:
                break
        except:
            print("it's not a number")
    print("You're right, the number is " + userNum)

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'Y':
        guess = randint(low,high)
        feedback = input (f"Is the number {guess} ? if it's not is it lower or higher (L/H), if it's correct Input (Y) :")
        if feedback == 'L':
            high = guess - 1
        elif feedback == 'H':
            low = guess + 1
        
    print ('Yay, i am correct!')    
        
    
guessNumber(10)
#computerGuess(10)
    

