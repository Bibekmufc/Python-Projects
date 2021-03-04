import os
import operator

from art import logo

print(logo)
auctionee = {}
bid_over = False

#initial loop to enter user input
while not bid_over:
    name = str(input("What is your name?\n"))
    try:
        bid = int(input('Please enter your bid.\n'))
    except ValueError:
        print('Please enter a valid numerical bid.')
    auctionee = {name: bid}

#second loop to check if there are new bidders
    new_entries = True
    while new_entries:
        new_entry = input("Are there any other bidders?\n")
        if not(new_entry in ['yes', 'no']) :
            print("You can only type either 'Yes' or 'No' ")
            continue
        else:
            if new_entry == "yes":
                    os.system('cls')
                    new_name = str(input("What is your name?\n"))
                    new_bid = int(input("What is your bid?\n"))
                    new_auctionee = {new_name: new_bid}
                    auctionee.update(new_auctionee)
                    continue
            if new_entry == "no":
                    win_name = max(auctionee, key = lambda key: auctionee[key])
                    highest_bid = max(auctionee.values())
                    print(f"The winner is {win_name} with a bid of {highest_bid}")
                    bid_over = True
                    break