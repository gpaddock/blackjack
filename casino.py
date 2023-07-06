import blackjack
import os

def bj(chips):
    clear()
    blackjack.play(chips)
    lobby(chips)


def bank():
    clear()
    print("Welcome to the bank!")
    print("How many BlueBucks would you like to buy?")
    print("1 BlueBuck = 1.75 USD = 1.61 EUR")
    print("1. 10 BlueBucks")
    print("2. 50 BlueBucks")
    print("3. 100 BlueBucks")
    print("...")
    print("4. Return to lobby")
    match int(input):
        case 1: chips += 10
        case 2: chips += 50
        case 3: chips += 100
        case 4: lobby(chips)
        

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
    match selection:
        case 1:
            bj(chips)
        case 9:
            bank(chips)
        case 0:
            print(f"Your {chips} BlueBucks won you:")
            print(f"{chips*1.75} USD or {chips * 1.61} EUR")
            print("Have a nice day!")
            exit()


if __name__ == "__main__":
    lobby(0)