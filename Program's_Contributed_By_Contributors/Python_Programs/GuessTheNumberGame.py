import random

print("Welcome to the number guessing game!")

# Generate a random number between 1 and 100.
number = random.randint(1, 100)

# Get the user's guess.
guess = int(input("Guess a number between 1 and 100: "))

# Keep looping until the user guesses the correct number.
while guess != number:
  # Check if the user's guess is too low or too high.
  if guess < number:
    print("Too low!")
  elif guess > number:
    print("Too high!")

  # Get the user's guess again.
  guess = int(input("Guess a number between 1 and 100: "))

# Print a message if the user guesses the correct number.
if guess == number:
  print("Congratulations! You guessed the number!")
