import random

game_number = random.randint(1,10)
print(game_number)
while(True):    
    user_guess = int(input(" Guess a number beetween 1 and 10: "))
    if user_guess > game_number:
        print("Too High")
    elif user_guess < game_number:
        print("too low")
    else:
        print("you win")