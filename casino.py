import blackjack
import os

def bj(chips):
    clear()
    blackjack.play(chips)
    lobby(chips)


def bank(chips):
    clear()
    print("Welcome to the bank!")
    print("How many BlueBucks would you like to buy?")
    print("1 BlueBuck = 1.75 USD = 1.61 EUR")
    print("10 BlueBucks")
    print("50 BlueBucks")
    print("100 BlueBucks")
    print("...")
    print("4. Return to lobby")
    amount = int(input())
    if amount == 4:
        lobby(chips)
    else:
        chips += amount
        

def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


def lobby(chips):
    clear()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Paddock Casino!")
    print(f"{chips} BlueBucks")
    print("What would you like to play?")
    print("1. Blackjack")
    print("...")
    print("9. Buy Chips")
    print("0. Cashout and Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    selection = int(input())
    if selection == 1:
        bj(chips)
    if selection == 2:
        bank(chips)
    if selection == 0:
        print(f"Your {chips} BlueBucks won you:")
        print(f"{chips*1.75} USD or {chips * 1.61} EUR")
        print("Have a nice day!")
        exit()


if __name__ == "__main__":
    lobby(0)