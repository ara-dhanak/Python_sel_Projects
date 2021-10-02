
import random
def guess_num(x):
    random_num = random.randint(1,x)
    guess = 0
    #while guess != random_num:
    for i in range(1,x+1):
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_num:
            print("Sorry Guess again, guess is low")
        elif guess > random_num:
            print(("Sorry Guess again,guess is high"))

    print("Correct guess")

guess_num(5)


