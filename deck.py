import card
import random

class Deck:

    def __init__(self):
        self.cards = []
        self.build_deck()

    def shuffle(self):
        random.shuffle(self.cards)

    def build_deck(self):
        for value in range(2, 15):
            for suit in range(4):
                new_card = card.Card(value, suit)
                self.cards.append(new_card)

    def draw_card(self):
        # TODO: deal with an empty list
        if len(self.cards) == 0:
            self.build_deck()
            self.shuffle()
        new_card = self.cards.pop(0)
        return new_card


