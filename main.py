import random

print('Welcome to the guessing game')
print("I'm thinking of a numver between 1 and 100, you need to guess it")
level = ''
while level != 'e' and level != 'h':
    level = input('Do you wnat (h)ard or (e)asy ? :')

if level == 'e':
    number_of_lives = 10

else:
    number_of_lives = 5

computer_guesses = random.randint(1,100)

player_wins = False

while number_of_lives >0 and not player_wins:
    player_guess = ''
    while not player_guess.isnumeric():
        player_guess = input(f"have a guess then {number_of_lives} guesses left")

    if int(player_guess) > computer_guesses:
        print("Your guess is higher than mine")
        number_of_lives-=1
        print(f"Number of lives remaining {number_of_lives}")

    elif int(player_guess)< computer_guesses:
        print(f"YOur guyess is lower than mine")
        number_of_lives-=1
        print(f"Number of lives remaining {number_of_lives}")

    else:
        print("Yes that's the one")
        player_wins = True



