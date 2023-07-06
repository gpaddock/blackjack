from card import Card
import random

class Deck:
    def __init__(self, num_decks):
        #initialize the deck with num_decks shuffled in together
        self.num_decks = num_decks

        #unshuffled
        deck = []
        for k in range(num_decks):
            for suit in ['He', 'Sp', 'Di', 'Cl']:
                for val in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                    deck.append(Card(suit, val))

        self.order = deck

    def display(self):
        i = 1
        for card in self.order:
            print(f"{i}: {card.suit}{card.val}")
            i += 1

    def shuff(self):
        random.shuffle(self.order)
    
    def deal(self) -> Card:
        if len(self.order) == 0:
            return 0
        else:
            if len(self.order) == 1:
                print("1 card remains in the deck!")
            return self.order.pop(0)


