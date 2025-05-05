# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

def calculation(auction_data):
    highest_price = 0
    winner = ''
    for person in auction_data:
        if auction_data[person] > highest_price:
            highest_price = auction_data[person]
            winner = person
    print(f"{winner} is the winner of the auction with a bid of {highest_price}")


bid = {}

should_continue = True
while should_continue:
    name = input("what is your name: \n").lower()
    price = int(input('what is your bid: $'))

    bid[name] = price

    # Input validation: only accept "yes" or "no"
    while True:
        another_bid = input("Is there another bid? Type 'yes' or 'no': ").lower()
        if another_bid in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if another_bid == "no":
        should_continue = False
        calculation(bid)
    elif another_bid == 'yes':
        print("\n" * 20)



