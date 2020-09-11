"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

# creating a list to store high scores
high_scores = []

def start_game():
  # setting the play_again variable to yes
  play_again = "y"
  
  print("Hello and welcome to The Guessing Game!!")
  
  # checking whether the player would like to play the game again. This will happen once by default
  while play_again != "n":
    # using the randint function from random to choose a random number between 1 and 10
    answer = random.randint(1,10)
    # print out the answer to hep with testing
#    print("The answer is {}.".format(answer))
    # print out the high scores list to help with testing
#    print(high_scores)
    guess = 0
    attempt = 0
    
    while guess != answer:
      # catching an error is the user does not input an integer
      try:
        guess = int(input("Pick a number between 1 and 10:  "))
      except ValueError:
        print("Hmm.. something went wrong. Try choosing a number between 1 and 10")
      else:
    
        # the first check is to see if the guess is within the expected range
        if guess < 1 or guess > 10:
          print("Your number should be between 1 and 10")
        # the second check is to see if the guess is less than the answer
        elif guess > answer:
          attempt += 1
          print("It's lower")
        # the third check is to see if the guess is more than the answer
        elif guess < answer:
          attempt += 1
          print("It's higher")
        # finally we can assert that the user correctly identified the answer
        # we output the number of attemps it took the user to guess the answer
        # we then output the current lowest high score
        # finally ask the user if they want to play again
        else:
          attempt += 1
          high_scores.append(attempt)
          print("You got it!")
          print("It took you {} guesses to find the answer.".format(attempt))
          print("The high score is {}.".format(min(high_scores)))
          play_again = input("Would you like to play again? (y/n):  ")
  # if the user no longer wants to play this will break out of the loop/function        
  else:
    if play_again == "n":
      print("Thank you for playing!")


# Kick off the program by calling the start_game function.
start_game()