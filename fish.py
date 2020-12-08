import deck
import random
import card

class GoFish:

    def __init__(self):
        self.deck_of_cards = deck.Deck()
        self.player_one = []
        self.player_two = []

    def play(self):
        self.deck_of_cards.shuffle()
        self.deal_cards()
        while len(self.player_one) > 0 and len(self.player_two) > 0:
            self.show_cards()
            self.player_one_turn()
            self.remove_fours(self.player_one)
            self.player_two_turn()
            self.remove_fours(self.player_two)

    def deal_cards(self):
        for x in range(5):
            card1 = self.deck_of_cards.draw_card()
            self.player_two.append(card1)
            card2 = self.deck_of_cards.draw_card()
            self.player_one.append(card2)

    def show_cards(self):
        print("Your cards:")
        for c in self.player_one:
            print(c)

    def player_one_turn(self):
        user_input = input("What is the rank of the card you ask for?")
        found = False
        for x in range(len(self.player_two)-1, -1, -1):
            if user_input == self.player_two[x].get_rank():
                found = True
                self.player_one.append(self.player_two[x])
                del self.player_two[x]
        if found == False:
            print("Go Fish")
            card2 = self.deck_of_cards.draw_card()
            self.player_one.append(card2)
        else:
            print("The player had that card!")

    def player_two_turn(self):
        ask_for = random.choice(self.player_two)
        print("Do you have any", ask_for.get_rank() + "'s?")
        found = False
        for x in range(len(self.player_one) - 1, -1, -1):
            if ask_for.get_rank() == self.player_one[x].get_rank():
                found = True
                self.player_two.append(self.player_one[x])
                del self.player_one[x]
        if found == False:
            print("Go Fish")
            card2 = self.deck_of_cards.draw_card()
            self.player_two.append(card2)
        else:
            print("The player had that card!")

    def remove_fours(self, hand):
        for x in range(len(hand)-1):
            count = 1
            for y in range(x+1, len(hand)):
                if hand[x].get_rank() == hand[y].get_rank():
                    count += 1
            if count == 4:
                for z in range(len(hand) - 1, -1, -1):
                    if hand[x].get_rank == hand[z].get_rank():
                        del hand[z]
                break





game = GoFish()
game.play()