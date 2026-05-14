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
print("Welcome to the Rock Paper Scissors game!")
game_images = [rock, paper, scissors]

while True:
    player = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
    computer = random.randint(0,2)
    print(f"You chose {game_images[player]}")
    print("Computer chose")
    print(game_images[computer])

    if player == 0 and computer == 1:
        print("Computer won")
    elif player == 0 and computer == 2:
        print ("Player won")
    elif player == 1 and computer == 2:
        print("Computer won")
    elif player == 1 and computer == 0:
        print("Player won")
    elif player == 2 and computer == 0:
        print("Computer won")
    elif player == 2 and computer == 1:
        print("Player won")
    else:
        print("Draw, try again")

    again = input("Do you want to play again? (y/n)").lower()
    if again == "no":
        print("Thanks for playing")
        break