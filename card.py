
class Card:
    # TODO - Add a compare method

    def __init__(self, value, suit):
        # TODO Deal with bad value and suite ranges
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.value = value
        self.suit_value = suit
        if value < 0 or value > 15:
            self.rank = self.ranks[0]
        else:
            self.rank = self.ranks[value-2]
        if suit < 0 or suit > 3:
            self.suit = self.suits[0]
        else:
            self.suit = self.suits[suit]

    def get_rank(self):
        return self.rank

    def compare(self, other):
        if self.value > other.value:
            return self.value - other.value
        elif other.value > self.value:
            return self.value - other.value
        else:
            if self.suit_value > other.suit_value:
                return self.suit_value - other.suit_value
            elif other.suit_value > self.suit_value:
                return self.suit_value - other.suit_value
            else:
                return 0

    def __str__(self):
        return self.rank + " of " + self.suit