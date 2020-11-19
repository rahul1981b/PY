from replit import clear
from art import logo
import random

easy_retries = 10
medium_retries = 7
hard_retries = 5
retries = 0

def set_difficulty_lavel():
  global retries
  diff_lavel = input("PLease enter difficulty lavel - easy, mediuma or hard: ")
  if diff_lavel == "easy":
    retries = easy_retries
  elif diff_lavel == "medium":
    retries = medium_retries
  elif diff_lavel == "hard":
    retries = hard_retries
  else:
    retries = 0
  
def play_game():
  clear()
  global retries
  print(logo)
  set_difficulty_lavel()
  print(f"You have got {retries} retries")
  number =  random.randint(0,200)
    
  while retries:
    user_number = int(input("Please guess the number: "))
    if user_number == number:
      print(f"You Got it right - number is {number}!")
      break
    elif user_number > number:
      if user_number > (1.5 * number):
        print("Too High")
      else:
        print("High")
    else:
      if user_number < (number/2):
        print("Too Low")
      else:
        print("Low")
    retries -= 1
  if (retries == 0):
    print(f"You lost - number was {number}. Better Luck next time :(")

play_game()

