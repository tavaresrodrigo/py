import random 
print ('Hello. What is your name?')
name = input()

print('Well, '+name+', I am thinking of a number between 1 and 10')
secretNumber = random.randint(1,11)
guessInput = 0

for guessTaken in range(1,4):
    try:
        print('Take a guess, you have 3 chances.')
        guess = int(input())
        guessInput = guess
        if guess < secretNumber:
            print ('Too low.')
        elif guess > secretNumber:
            print ('To high.')
        else:
            break
    except ValueError:
        print('You must inform a valid number')

if guessInput == secretNumber:
    print('Good job '+name+'! You guessed my number in '+str(guessTaken)+' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

