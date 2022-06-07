import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1-9")
while chances <5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You won!")
        break
    elif guess < number:
        print("Your guess was too low! Guess a higher number!")
    else:
        print("Your guess was too high! Guess a lower number!")

    chances +=1

    if not chances <5:
        print("You lose! The number is: ", number)

    
    
