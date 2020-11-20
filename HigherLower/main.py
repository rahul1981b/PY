from game_data import data
from art import logo, vs
import random

def play_game():
  should_continue_game = True
  while should_continue_game == True:
    print(logo)
    opt1 = random.choice(data)
    opt2 = random.choice(data)
    s1 = opt1['follower_count']
    print(f"compare A: {opt1['name']}, a {opt1['description']}, from {opt1['country']}")
    print(vs)
    s2 = opt2['follower_count']
    print(f"compare B: {opt2['name']}, a {opt2['description']}, from {opt2['country']}")
    ch = input("Who has more follower? Type 'A' or 'B': ")
    if ch == 'A' and s1 > s2:
      print("You Won!")
    elif ch == 'A' and s1 < s2:
      print("You Lost!")
      should_continue_game = False
    elif ch == 'B' and s2 > s1:
      print("You Won!")
    else:
      print("You Lost :(")
      should_continue_game = False
play_game()