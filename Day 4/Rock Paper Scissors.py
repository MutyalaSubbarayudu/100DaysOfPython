import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int ( input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n") )

game_control_list = [rock,paper,scissors]

if user_input >=3 or user_input < 0:
  print("Invalid Input, You lose")
else:
  print(game_control_list[user_input])

  bot_input =  random.randint(0,2)

  print("Computer Chose: \n")

  print(game_control_list[bot_input])

  if user_input==bot_input:
    print("Its a draw")
  elif user_input == 0:
    if bot_input == 1:
      print ("You lose")
    elif bot_input == 2:
      print ("You win")
  elif user_input == 1:
    if bot_input == 0:
      print("You win")
    elif bot_input == 2:
      print("You lose")
  elif user_input == 2:
    if bot_input == 0:
      print("You lose")
    elif bot_input == 1:
      print("You win")


  if user_input == bot_input:
    print("Its a Draw")
  elif (user_input == 0 and bot_input == 1 ) or ( user_input == 1 and bot_input == 2) or (user_input == 2 and bot_input == 0):
    print ("You Lose")
  elif (user_input == 0 and bot_input == 2) or (user_input ==1 and bot_input == 0) or (user_input == 2 and bot_input == 1):
    print("You Win")

