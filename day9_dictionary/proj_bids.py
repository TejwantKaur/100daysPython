import os

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')


bids = {}
bids_finish = False

def find_highest(bids):
    highest_bid = 0
    winner = ""

    for i in bids:
        amt = bids[i]
        if amt > highest_bid:
            highest_bid = amt
            winner = i

    print(f"The winner is {winner} with thw bid of ${highest_bid}")

while not bids_finish:
    name = input("Enter your name: ")
    price = int(input("What is your bid $"))
    bids[name] = price 
    # name is string already and price int

    should_continue = input("Are there any other for bid? 'y' 'n': ").lower()

    if should_continue == 'n':
        bids_finish = True
        print(find_highest(bids))
    elif should_continue == 'y':
        clear()
