from deck import Deck
import random

def bet(chips)-> float:
   print(f"You have {chips} BlueBucks,")
   print("how many would you like to bet?")
   amount = int(input())
   if amount > chips:
      print("You cannot bet that much!")
      bet(chips)
   else: 
      chips = chips - amount
      return amount



def play(chips):
   # Initialize game
   players = random.randint(0, 5)
   print("Hello and welcome to blackjack!")
   print(f"{players} players sit at the table today")
   print("How many decks would you like to play with?")
   num_decks = input(num_decks)
   deck = Deck(num_decks)
   # Betting phase
   amount_bet = bet()
   # Play a round
   
