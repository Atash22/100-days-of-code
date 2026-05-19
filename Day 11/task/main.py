import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' \n")
if start == 'y':
    print(logo)

    player_hand = [random.choice(cards), random.choice(cards)]
    comp_hand = [random.choice(cards)]
    print(f"Your cards: [{player_hand}], current score:{sum(player_hand)}")
    print(f"Computer's first card: {comp_hand}")

    while sum(player_hand) < 21:
        another_card = input(f"Type 'y' to get another card or type 'n' to pass \n")
        if another_card == 'y':
            player_hand.append(random.choice(cards))
            print(f"Your cards: [{player_hand}], current score:{sum(player_hand)}")
            print(f"Computer's first card: {comp_hand}")
        else:
            break

    while sum(comp_hand) < 21:
        comp_hand.append(random.choice(cards))


    player_score = sum(player_hand)
    comp_score = sum(comp_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {comp_hand}, final score: {comp_score}")

    if player_score == comp_score:
        print("Draw")
    elif player_score > 21:
        print("You went over 21, you lose! :(")
    elif comp_score > 21:
        print("Computer went over 21, You win!:)")
    elif player_score > comp_score:
        print("You win!:)")
    else:
        print("You lose! :(")