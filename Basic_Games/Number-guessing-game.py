import random

no_of_guesses=0
print("Enter the range in between you want to guess the number: ")
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
c_guess = random.randint(lower, upper)
while True:
    p_guess = int(input("Enter a number: "))
    if p_guess == c_guess:
        print("You guessed the number.")
        no_of_guesses += 1
        break
    elif p_guess<(c_guess/2):
        print("You guessed a bit to less")
        no_of_guesses += 1
        continue
    elif p_guess>(c_guess/2) and p_guess<c_guess:
        print("guess a number bigger")
        no_of_guesses += 1
        continue
    elif p_guess>(c_guess*2):
        print("You guessed are a pretty large number")
        no_of_guesses += 1
        continue
    elif p_guess<(c_guess*2) and p_guess>c_guess:
        print("Think of a smaller number")
        no_of_guesses += 1
        continue
    else:
        print("Invalid input, enter a valid input")
        continue
    
print(f"No. of guesses = {no_of_guesses}")