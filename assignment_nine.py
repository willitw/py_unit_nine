# assignment_nine.py
# Twig Williams
# 1/18/2024
# Simulates a game of compare/war between 2 players

from deck import CardDeck  # Import the CardDeck class from deck.py

colored_suit_symbols = {'♣': '♣️', '♦': '♦️', '♥': '♥️', '♠': '♠️'}                                                        # Mapping of standard suit emojis to the colored versions
card_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}  # Mapping of card ranks to numerical values
card_suit_rank = {colored_suit_symbols[suit]: i + 1 for i, suit in enumerate(['♣', '♦', '♥', '♠'])}                         # Mapping the suit symbols to ranks

def compare_cards(player1_card, player2_card):
    """
    Compare two cards based on rank and suit.

    Parameters:
    - player1_card (dict): Dictionary representing the card of Player 1.
    - player2_card (dict): Dictionary representing the card of Player 2.

    Returns:
    - bool: True if Player 2 wins the round, False otherwise.
    """
    if player1_card['rank'] == player2_card['rank']:                                        # Checking if ranks are equal
        return card_suit_rank[player1_card['suit']] < card_suit_rank[player2_card['suit']]  # Comparing suits if ranks are equal
    else:
        return card_rank[player1_card['rank']] < card_rank[player2_card['rank']]            # Comparing ranks if ranks are not equal

def play_round(player1_hand, player2_hand):
    """
    Play one round of the game.

    Parameters:
    - player1_hand (list): List representing Player 1's hand.
    - player2_hand (list): List representing Player 2's hand.

    Returns:
    - int: 2 if Player 2 wins the round, 1 if Player 1 wins the round.
    """
    player1_card = player1_hand.pop(0)                                     # Removing the first card from Player 1's hand
    player2_card = player2_hand.pop(0)                                     # Removing the first card from Player 2's hand

    print(f"Player 1: {player1_card['rank']} of {player1_card['suit']}")   # Displaying Player 1's card
    print(f"Player 2: {player2_card['rank']} of {player2_card['suit']}")   # Displaying Player 2's card

    if compare_cards(player1_card, player2_card):                          # Comparing the two cards
        print("\033[92mPlayer 2 wins this round!\033[0m")                  # Displaying round winner
        return 2
    else:
        print("\033[92mPlayer 1 wins this round!\033[0m")                  # Displaying round winner
        return 1


# I used chatgpt for a little of the main game logic
def play_game_compare():
    """
    Play the game of Compare.

    Allows the player to decide the number of cards and plays rounds until there's a winner.
    """
    print("Welcome to the game of Compare. You will decide how many cards we get, and then we'll play them one by one.")    # print the welcoming to the player
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.\n")                     # print the game instructions

    while True:
        try:
            num_cards = int(input("How many cards should each player get? Enter a number between 1 and 26:"))  # Taking input for the number of cards
            if 1 <= num_cards <= 26:                                                                           # Validating input range
                break
            else:
                print("Please enter a number between 1 and 26.")                                               # Prompt for a valid input
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 26.")                                    # Handling invalid input

    deck = CardDeck()                                                                                          # Initializing and shuffling the card deck
    deck.shuffle_deck()

    player1_hand = deck.deal_cards(num_cards)                                                                  # Dealing cards to Player 1
    player2_hand = deck.deal_cards(num_cards)                                                                  # Dealing cards to Player 2

    print(f"Dealer deals {num_cards} cards to each player...")                                                 # Displaying the dealing process
    print(f"\nPlayer 1 Hand: {' '.join([card['rank'] + ' of ' + card['suit'] for card in player1_hand])}")     # Displaying Player 1's hand
    print(f"Player 2 Hand: {' '.join([card['rank'] + ' of ' + card['suit'] for card in player2_hand])}")       # Displaying Player 2's hand

    rounds_won_player1 = 0                                                                                     # Variables to track the number of rounds won by each player
    rounds_won_player2 = 0
    round_num = 1                                                                                              # Main game loop

    while player1_hand and player2_hand:
        print(f"\nRound {round_num}:")                                                                         # Displaying the current round
        round_winner = play_round(player1_hand, player2_hand)                                                  # Playing one round and determining the winner

        if round_winner == 1:                                                                                  # Updating round winner statistics
            rounds_won_player1 += 1
        else:
            rounds_won_player2 += 1

        round_num += 1

    print("\nGame Over!")                                                                                      # Showing the end of the game
    print(f"Player 1 wins: {rounds_won_player1} rounds")                                                       # Displaying Player 1's total wins
    print(f"Player 2 wins: {rounds_won_player2} rounds")                                                       # Displaying Player 2's total wins

    if rounds_won_player1 > rounds_won_player2:                                                                # Determining the overall game winner
        print("\033[92mPlayer 1 wins the game!\033[0m")                                                        # Displaying the overall game winner (Player 1)
    elif rounds_won_player2 > rounds_won_player1:
        print("\033[92mPlayer 2 wins the game!\033[0m")                                                        # Displaying the overall game winner (Player 2)
    else:
        print("It's a tie!")                                                                                   # Displaying a tie result

def main():
    play_game_compare()

main()
