"""
This program will analyse the probabilty on whether you will lose
depending on your hand and the dealers hand. Many samples are taken from
each hand and then developed

Object oriented or procedual?

1. Ask how many decks?
2. How many samples per hand combo?
3. Draw player cards. Takes first card from top row
3.5. How does the player know when to stop playing?
4. Draw dealer cards. Takes first card from second row.
5. If win +1, if loss +0, if tie +?
6. Display hand combinations and their results

"""
import random
from copy import deepcopy
ROYALS = ["K", "Q", "J"]
DECK_SLEEVE = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
sample_totals = []
DECK = []
wins = 0
player_hand = []
dealer_hand = []


decks = int(input("How many decks?(>=1): "))

sample_size = int(input("How many samples per hand combo?: "))

for i in range(decks*4):
    DECK.append(DECK_SLEEVE)

deck_rows = len(DECK)
deck_cards = len(DECK_SLEEVE)


def total_hand(hand):
    total = 0

    for index, cards in enumerate(hand):

        total += cards

    return total


def convert(card):
    if card in ROYALS:
        card = 10
    elif card == "A":
        card = 11
    else:
        return card

    return card


for index1, dealer_card in enumerate(DECK_SLEEVE):
    for index2, player_card in enumerate(DECK_SLEEVE):
        # Set the starting hand Cards
        sample_totals.append([str(dealer_card), str(player_card)])
        deck_copy = deepcopy(DECK)

        player_card = convert(player_card)

        dealer_card = convert(dealer_card)
        player_hand.append(player_card)
        dealer_hand.append(dealer_card)
        deck_copy[0][index2] = "o"
        deck_copy[1][index1] = "o"

        # Start the sampling
        sample_deck = deepcopy(deck_copy)
        #print(dealer_card, player_card)
        for sample in range(sample_size):
            #print(f"Sample...{sample}")
            # print(player_hand, dealer_hand)

            player_hand_size = total_hand(player_hand)
            dealer_hand_size = total_hand(dealer_hand)
            while player_hand_size < 17:
                # Begin dealing the player a card

                row = random.randint(0, deck_rows-1)
                column = random.randint(0, deck_cards-1)
                card = sample_deck[row][column]

                # Make sure there is a card there
                while card == "o":
                    row = random.randint(0, deck_rows - 1)
                    column = random.randint(0, deck_cards - 1)
                    card = sample_deck[row][column]
                card = convert(card)
                player_hand.append(card)
                player_hand_size = total_hand(player_hand)
                if player_hand_size > 21 and 11 in player_hand:
                    eleven_index = player_hand.index(11)
                    player_hand[eleven_index] = 1
                    player_hand_size = total_hand(player_hand)


                sample_deck[row][column] = "o"

            while dealer_hand_size < 17:
                # Begin dealing the player a card

                row = random.randint(0, deck_rows - 1)
                column = random.randint(0, deck_cards - 1)
                card = sample_deck[row][column]

                # Make sure there is a card there
                while card == "o":
                    row = random.randint(0, deck_rows - 1)
                    column = random.randint(0, deck_cards - 1)
                    card = sample_deck[row][column]
                card = convert(card)
                dealer_hand.append(card)
                dealer_hand_size = total_hand(dealer_hand)
                # If they have an ace convert it to a 1
                if dealer_hand_size > 21 and 11 in dealer_hand:
                    eleven_index = dealer_hand.index(11)
                    dealer_hand[eleven_index] = 1
                    dealer_hand_size = total_hand(dealer_hand)

                sample_deck[row][column] = "o"



            if player_hand_size > 21:
                wins += 0
            elif player_hand_size == 21:
                wins += 1
            elif player_hand_size >= dealer_hand_size:
                wins += 1
            elif player_hand_size < dealer_hand_size and dealer_hand_size > 21:
                wins += 1
            """
            print(f"Player: {player_hand}, {player_hand_size}")
            print(f"Dealer: {dealer_hand, dealer_hand_size}")
            print(wins/(sample_size))
            print("")
            """

            # Reset the player hand and dealer hand

            player_hand = [player_card]
            dealer_hand = [dealer_card]
            sample_deck = deepcopy(deck_copy)
        # Set the percentage for the starting hand
        sample_totals[-1].append((wins/sample_size)*100)
        # print(sample_totals)
        wins = 0
        player_hand = []
        dealer_hand = []


for i in sample_totals:
    print(f"Dealer: {i[0]}, Player: {i[1]}, PlayerWinPercent: {i[2]}")

most_likely_win = ""
least_likely_win = ""

for i in sample_totals:
    if len(most_likely_win) == 0:
        most_likely_win = i
    if len(least_likely_win) == 0:
        least_likely_win = i

    if most_likely_win[2] < i[2]:
        most_likely_win = i
    if least_likely_win[2] > i[2]:
        least_likely_win = i


print(f"Most Likely Win: Dealer: {most_likely_win[0]}, Player: {most_likely_win[1]} Percen: {most_likely_win[2]}")
print(f"Least Likely Win: Dealer: {least_likely_win[0]}, Player: {least_likely_win[1]} Percen: {least_likely_win[2]}")

