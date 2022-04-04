import random

#Ask for player name and guess.
player_name = input("What is your name? \n")
print(f"Hello {player_name}, I am thinking of a number between 0 - 20. Take a guess.")

#Generates random number

random_number = random.randint(0,20)


#for loop to give player 5 tries

for guesstaken in range(1, 6):
    player_guess = int(input())
    if player_guess > random_number:
        print("Your guess is too high")
    elif player_guess < random_number:
        print("your guess is too low")
    else:
        break #breaks of the loop when right number is guessed.

#player guess the right nume
if player_guess == random_number:
    print(f"That is the right number! You took {guesstaken} tries. Great Job {player_name}!")
#When player runs out of tries. Prints out the random number.
else:
    print(f"Nope, the number I was thinking of is {random_number}")
 
