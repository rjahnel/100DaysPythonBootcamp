import clear

def find_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for name in bids:
        bid = bids[name]
        if  bid > highest_bid:
            highest_bid = bid
            winner = name

    print (f"The winner ist {winner} with a bid of ${highest_bid}.")

another_bid = True
bid_dict = {}

while another_bid:
    clear.cls()
    name = input("Name: ")
    bid_price = int(input("Bid Price: $"))
    bid_dict[name] = bid_price

    another_user = input("Another user to bid? (yes/no): ".lower())
    if another_user != "yes":
        another_bid = False

find_highest_bid(bid_dict)