#class for individual card objects, decks are lists of cards

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val