from deck import Deck
import random
from player import Player

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



def begin(chips):
   # Initialize game with random players and random amount
   players = [Player(random.randint(-3,2)) for _ in random.randint(0, 5)]
   print("Hello and welcome to blackjack!")
   print(f"{len(players)} players sit at the table today")
   print("How many decks would you like to play with?")
   num_decks = input(num_decks)
   deck = Deck(num_decks)
   again = 1
   while(again == 1):
      # Betting phase
      amount_bet = bet()
      # Play a round
      win = play_round(chips)
      chips += (-1 * amount_bet) if not win else amount_bet
      print("Play again?")
      print("0. Exit")
      print("1. Another Round!")
      again = int(input())

   

def play_round(chips, players)-> bool:
   #add one hand for dealer
   hands = [[] for _ in range(len(players))]
   for i in range(2):
      for k in range(len(hands)):
         hands[k].append(Deck.deal())
   
   print()
