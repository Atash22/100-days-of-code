from art import logo
print(logo)
    # TODO-1: Ask the user for input

    # TODO-2: Save data into dictionary {name: price}

    # TODO-3: Whether if new bids need to be added

    # TODO-4: Compare bids in dictionary
bidding_dictionary = {}
def announce_winner():
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bidding = bidding_dictionary[winner]
    print(f"The winner is {winner} with ${highest_bidding}")


def bidding():
    bedding_finished = False
    while not bedding_finished:
        name = input("What's your name?\n")
        bid = int(input("How much would you like to bid?\n"))
        bidding_dictionary[name] = bid
        new_bid = input("Are there other users you want to add? Yes, No\n").lower()
        if new_bid == "yes":
            print("\n" * 50)
        else:
            bedding_finished = True
    announce_winner()
bidding()