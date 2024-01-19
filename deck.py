# deck.py
# Twig Williams
# 1/18/2024

import random

colored_suit_symbols = {'♣': '♣️', '♦': '♦️', '♥': '♥️', '♠': '♠️'} # Mapping standard suits to their colored versions

class CardDeck:
    def __init__(self):
        """
        Initialize a standard deck of cards with ranks and suits.

        The deck is a list of dictionaries, where each dictionary represents a card.
        """
        self.suits = ['♣', '♦', '♥', '♠']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [{'rank': rank, 'suit': colored_suit_symbols[suit]} for rank in self.ranks for suit in self.suits]

    def shuffle_deck(self):
        """
        Shuffle the deck using the Fisher-Yates shuffle algorithm.

        This method modifies the order of cards in the deck.
        """
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal_cards(self, num_cards):
        """
        Deal a specified number of cards from the deck.

        Parameters:
        - num_cards (int): The number of cards to be dealt.

        Returns:
        - list: A list of dictionaries representing the dealt cards.
        """
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

