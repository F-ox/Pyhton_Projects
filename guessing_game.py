def start_game():

  print("--------------------------------------\n Welcome to the Number Guessing Game! \n --------------------------------------")


  try:
    name= input("What's your name? ")
    print("Hi {}, my name is HAL 9000 *beep* *boop*. \n I am thinking of a number between 1 and 10, can you guess which number it is? *beep* *boop*? \n...Are your ready?".format(name))
  except NameError:
    print("Oops, this is not a correct name:)")
    name= input("What's your name? ")

  import random
  import sys
  from random import randrange

  attempts = 1

  answer = randrange(1,10)

  try:
    guess = int(input("...What is the number? "))
  except ValueError:
    print("Oops, this is not a correct value, please enter a number between 1 and 10 :)")
    guess = int(input("...What is the number? "))

  while guess != answer:

    if guess > answer:
      print("Too high, guess again.")
      attempts += 1
      guess = input("...What is the number? ")
      guess = int(guess)
      continue

    if guess < answer:
      print("Too low, guess again.")
      attempts += 1
      guess = input("...What is the number? ")
      guess =int(guess)
      continue

    if guess == answer:
      break

  if guess == answer:
    print("You got it! {}, is the correct answer *beep* *boop*!".format(answer))
    print("Tries: {}".format(attempts))
    try:
      try_again = input("Would you like to play again? (Y/N): ")
    except ValueError:
      print("Oops,this is not a correct command, please type Y for yes or N for no :)")
    except NameError:
      print("Oops,this is not a correct command, please type Y for yes or N for no :)")
    else:
      if try_again == "Y":
        start_game()    
      if try_again == "N":
        print("No worries, See you later {}!".format(name))
        sys.exit()

      
start_game()
