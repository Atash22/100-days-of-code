from art import logo
from art import vs
from game_data import data
import random
print(logo)

def higher_lower():
    score = 0
    while True:

        a = random.randint(0, 50)
        b = random.randint(0, 50)
        print(f"Compare: A: {data[a]["name"]}, {data[a]["description"]}, {data[a]["country"]}")
        print(vs)
        print(f"Against: B: {data[b]["name"]}, {data[b]["description"]}, {data[b]["country"]}")
        guess = input("Who has more followers: 'A' or 'B'").lower()
        a_follower = data[a]["follower_count"]
        b_follower = data[b]["follower_count"]

        if guess == "a" and a_follower > b_follower:
            score += 1
            print(f"Your score: {score}")
        elif guess == "b" and b_follower > a_follower:
            score += 1
            print(f"Your score: {score}")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            return False



higher_lower()