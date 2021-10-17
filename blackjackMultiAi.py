# So lets make an AI for this Black Jack

import random
import time
from copy import copy, deepcopy

# First lets make an array of the deck
riskLimit = 50
cont = 0
total = 0
deck = [
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Hearts
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Diamonds
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Spades
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Hearts
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Diamonds
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Spades
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Hearts
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Diamonds
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Spades
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Hearts
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Diamonds
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Spades
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Hearts
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Diamonds
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Spades
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Hearts
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Diamonds
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],  # Spades
    ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    # Clubs
]
aiWin = 0
aiLose = 0

# Doubling down is actually more simple than I thought it would


def findCardSuit():
    suits = []
    for i in range(0, len(deckUsing)):
        suits.append(i)

    card = []
    count = 0
    # Here when it picks a new card I could get it to pick a card until it picks one with in the range rather than
    # messing with this
    # If cards are taken out of the first row, then will product a shorter list which may not have all the possible
    # choices. Go through deckUsing and assign it to a count value. if the one is larger than the previous, replace it.
    # Redo this. First Find the suit wanted, create a list of the index of that list
    for counting in deckUsing:
        newcountindex = deckUsing.index(counting)
        newcount = len(deckUsing[newcountindex])
        if newcount > count:
            count = newcount
    for i in range(0, newcount):
        card.append(i)

    return [suits, card]


# Rather
# RiskValue - Calculated by the AI to determine if it should pick up another card, If lower than 50% risk, pick up.
# Create arrays with the length of the array with a for i in deck: suits.append(i)
playing = int(input("How many players playing? \n "))
yourMoney = {}

for i in range(1, (playing + 1)):
    yourMoney[str(i)] = 10

aiPlaying = int(input("How many AI players? \n"))

aiMoney = {}
for i in range(1, (aiPlaying + 1)):
    aiMoney[str(i)] = 10

while True:
    bettingPool = 0
    yourHand = {}
    shadowHand = {}
    yourScore = {}
    yourLeader = {}
    yourBet = {}
    getWon = 0
    # make it so players can make a bet
    for i in range(1, (playing + 1)):
        yourHand[str(i)] = []
        shadowHand[str(i)] = []
        yourScore[str(i)] = 0
        yourLeader[str(i)] = ""
        yourBet[str(i)] = 0

    aiHand = {}

    aiScore = {}
    aiLeader = {}
    aiBet = {}
    aiRisk = {}
    for i in range(1, (aiPlaying + 1)):
        aiHand[str(i)] = []

        aiScore[str(i)] = 0
        aiLeader[str(i)] = ""
        aiBet[str(i)] = 0
        aiRisk[str(i)] = 0
    deckUsing = deepcopy(deck)
    cardInfo = findCardSuit()
    turn = 'play'

    # First deal 2 cards to the AI and remove them from the list.
    # This is a bit hacky can be changed later
    # make a function called draw()
    # draw House Hand
    suit1 = random.choice(cardInfo[0])
    suit2 = random.choice(cardInfo[0])
    type1 = random.choice(cardInfo[1])
    type2 = random.choice(cardInfo[1])
    # Check that they aren't the same card. Very Low chance but still.
    while suit1 == suit2 and type1 == type2:
        suit1 = random.choice(cardInfo[0])
        suit2 = random.choice(cardInfo[0])
        type1 = random.choice(cardInfo[1])
        type2 = random.choice(cardInfo[1])
    hand = [deckUsing[suit1][type1], deckUsing[suit2][type2]]
    deckUsing[suit1].remove(hand[0])
    deckUsing[suit2].remove(hand[1])
    # Do AI hands
    for key in aiHand:
        if aiMoney[key] <= 0.01:
            continue
        else:
            cardInfo = findCardSuit()
            suit1 = random.choice(cardInfo[0])
            suit2 = random.choice(cardInfo[0])
            type1 = random.choice(cardInfo[1])
            type2 = random.choice(cardInfo[1])
            # Check that they aren't the same card. Very Low chance but still.
            while suit1 == suit2 and type1 == type2:
                suit1 = random.choice(cardInfo[0])
                suit2 = random.choice(cardInfo[0])
                type1 = random.choice(cardInfo[1])
                type2 = random.choice(cardInfo[1])
            while type1 >= len(deckUsing[suit1]) or type2 >= len(deckUsing[suit2]) or suit1 >= len(deckUsing) or suit2 >= len(deckUsing):
                suit1 = random.choice(cardInfo[0])
                suit2 = random.choice(cardInfo[0])
                type1 = random.choice(cardInfo[1])
                type2 = random.choice(cardInfo[1])
                while suit1 == suit2 and type1 == type2:
                    suit1 = random.choice(cardInfo[0])
                    suit2 = random.choice(cardInfo[0])
                    type1 = random.choice(cardInfo[1])
                    type2 = random.choice(cardInfo[1])
            aiHand[key] = [deckUsing[suit1][type1], deckUsing[suit2][type2]]
            deckUsing[suit1].remove(deckUsing[suit1][type1])
            deckUsing[suit2].remove(deckUsing[suit2][type2])

    # Remove card from the copied deck
    # Now draw the players cards.
    for key in yourHand:
        if yourMoney[key] <= 0.01:
            continue
        else:
            cardInfo = findCardSuit()
            suit1 = random.choice(cardInfo[0])
            suit2 = random.choice(cardInfo[0])
            type1 = random.choice(cardInfo[1])
            type2 = random.choice(cardInfo[1])

            while suit1 == suit2 and type1 == type2:
                suit1 = random.choice(cardInfo[0])
                suit2 = random.choice(cardInfo[0])
                type1 = random.choice(cardInfo[1])
                type2 = random.choice(cardInfo[1])
            # This checks that it isn't out of range
            while type1 >= len(deckUsing[suit1]) or type2 >= len(deckUsing[suit2]) or suit1 >= len(
                    deckUsing) or suit2 >= len(deckUsing):
                suit1 = random.choice(cardInfo[0])
                suit2 = random.choice(cardInfo[0])
                type1 = random.choice(cardInfo[1])
                type2 = random.choice(cardInfo[1])
                while suit1 == suit2 and type1 == type2:
                    suit1 = random.choice(cardInfo[0])
                    suit2 = random.choice(cardInfo[0])
                    type1 = random.choice(cardInfo[1])
                    type2 = random.choice(cardInfo[1])

            yourHand[key] = [deckUsing[suit1][type1], deckUsing[suit2][type2]]
            shadowHand[key] = [deckUsing[suit1][type1], deckUsing[suit2][type2]]

            deckUsing[suit1].remove(deckUsing[suit1][type1])
            deckUsing[suit2].remove(deckUsing[suit2][type2])
    total = 0

    score = 0
    # Betting Pool will take 1 chip from each player. If multiple winners are found. The winners get to keep their chips
    # While losers give their chips to the house
    for x in hand:
        cards = hand.index(x)
        if x == 'K' or x == 'Q' or x == 'J':
            hand[cards] = 10
        if x == 'A':
            hand[cards] = 11
        score += hand[cards]
    # Will convert any values for Ai hands into numerical values
    for key, value in aiHand.items():
        if aiMoney[key] <= 0.01:
            continue
        else:
            newHand = aiHand[key]

            playerScore = 0
            for i in newHand:
                cardIndex = newHand.index(i)
                if i == 'K' or i == 'Q' or i == 'J':
                    newHand[cardIndex] = 10
                if i == 'A':
                    newHand[cardIndex] = 11
                playerScore += newHand[cardIndex]
                aiHand[key] = newHand
                aiScore[key] = playerScore

    # Shadow hand is where the calculations occur
    for key, value in shadowHand.items():
        if yourMoney[key] <= 0.01:
            continue
        else:
            newHand = shadowHand[key]
            playerScore = 0
            for i in newHand:
                cardIndex = newHand.index(i)
                if i == 'K' or i == 'Q' or i == 'J':
                    newHand[cardIndex] = 10
                if i == 'A':
                    newHand[cardIndex] = 11
                playerScore += newHand[cardIndex]
                shadowHand[key] = newHand
                yourScore[key] = playerScore

    for x in deckUsing:
        position = deckUsing.index(x)

        total += len(deckUsing[position])

    perDict = {}

    # Could turn this into a function called perCal()
    for k in deckUsing:

        position = deckUsing.index(k)
        # print(k)
        # print(position)
        for y in deckUsing[position]:
            key = y
            # Find if it is not in the dictionary, if so then add a new key
            # Any non-integer values are converted to their integer value
            if key == 'J' or key == 'Q' or key == 'K':
                key = 10
            elif key == 'A':
                key = 1

            if key not in perDict:
                # print(y)
                perDict[key] = deckUsing[position].count(y)

            else:  # The key is already in the dictionary so add it to a previous key     print(y)

                perDict[key] = perDict[key] + deckUsing[position].count(y)

    # To get Percentage: Make a dictionary, each key is related to the corresponding number,
    # Convert J Q K A into number keys
    # Calculate Risk: How of a chance that the next card will make them go bust
    # Calculate the percentage chance for each number, add all the numbers together that will make them go bust
    # if the risk is lower than the set value go for another, if not stay.
    for key, value in yourBet.items():
        if yourMoney[key] <= 0.01:
            continue
        else:
            while True:
                bet = float(input(
                    "Player " + str(key) + ", What is your bet? \nCurrent Money: " + str(yourMoney[key]) + " \n>>> "))
                if bet > yourMoney[key]:
                    print('Please add less.')
                if bet < 0.01:
                    print('Please add more.')
                else:
                    yourMoney[key] -= bet
                    yourBet[key] = bet
                    break

    for key, value in aiBet.items():
        if aiMoney[key] <= 0.01:
            continue
        else:

            # Create a list for their possible bet choices

            # if an AI Wins there value is no longer an integer, so maybe times the money by a value between (0,1]
            while True:
                bet = random.random() * aiMoney[key]
                if bet >= 0.01:
                    break
            aiMoney[key] -= bet
            aiBet[key] = bet
            print('Ai bet ' + str(bet))

    for player, hands in aiHand.items():
        if aiBet[player] < 0.01:
            continue
        else:
            while True:
                aiRisk[player] = 0
                perDict = {}
                for k in deckUsing:

                    position = deckUsing.index(k)
                    # print(k)
                    # print(position)
                    for y in deckUsing[position]:
                        key = y
                        # Find if it is not in the dictionary, if so then add a new key
                        if key == 'J' or key == 'Q' or key == 'K':
                            key = 10
                        elif key == 'A':
                            key = 1

                        if key not in perDict:
                            # print(y)
                            perDict[key] = deckUsing[position].count(y)

                        else:  # The key is already in the dictionary so add it to a previous key     print(y)

                            perDict[key] = perDict[key] + deckUsing[position].count(y)
                for key, value in perDict.items():
                    perDict[key] = (value / total) * 100

                    # Find what key are greater than 21 - score
                    # Make the RiskLimit Lower if the current score is higher
                    # newRiskLimit = riskLimit - (score * rand)
                    if key > (21 - aiScore[player]):
                        # Make a value aiRisk to replace risk and avoid
                        aiRisk[player] += perDict[key]
                print(perDict)

                print('It is AI ' + str(player) + " turn.")
                print('AI Hand: ' + str(hands))
                print("AI score: " + str(aiScore[player]))
                print('AI Money: ' + str(aiMoney[player]))
                print("Current Risk: " + str(aiRisk[player]))
                print("")
                print("")
                print("")

                time.sleep(2)
                # Now to create the turns. If the AI wants to play a another
                # Count the amount of aces if they have them here before it gets into the if statements
                if aiScore[player] > 21:
                    print('AI ' + str(player) + ' went Bust')
                    print("")
                    print("")
                    print("")

                    time.sleep(1)
                    break
                if aiScore[player] == 21:
                    print('AI scored BlackJack')
                    print("")
                    print("")
                    print("")
                    time.sleep(1)
                    break
                if aiRisk[player] <= riskLimit:

                    print('AI ' + str(player) + ' Draws')
                    print("")
                    print("")
                    print("")
                    cardInfo = findCardSuit()
                    suit1 = random.choice(cardInfo[0])
                    type1 = random.choice(cardInfo[1])
                    # Find if the index is not in the equation
                    while type1 >= len(deckUsing[suit1]):
                        suit1 = random.choice(cardInfo[0])
                        type1 = random.choice(cardInfo[1])
                    theKey = aiHand[player]
                    theKey.append(deckUsing[suit1][type1])
                    aiHand[player] = theKey
                    deckUsing[suit1].remove(deckUsing[suit1][type1])
                    perDict = {}

                    # Change this to the new system
                    for key, value in aiHand.items():
                        if aiBet[key] <= 0:
                            continue
                        else:
                            newHand = aiHand[key]
                            playerScore = 0
                            for i in newHand:
                                cardIndex = newHand.index(i)
                                if i == 'K' or i == 'Q' or i == 'J':
                                    newHand[cardIndex] = 10
                                if i == 'A':
                                    newHand[cardIndex] = 11
                                playerScore += newHand[cardIndex]

                            while playerScore > 21:
                                if 11 in newHand:
                                    handIndex = newHand.index(11)
                                    newHand[handIndex] = 1
                                    playerScore -= 10
                                else:
                                    break
                            # Something Different: while playerScore > 21
                            aiHand[key] = newHand
                            aiScore[key] = playerScore

                else:
                    print('AI Folds')
                    break

        # Start the player code from here. Enable multiple people by using a
        # Dictionary with each key representing the respective players hand
        # yourHand = {"player1":[1,1]
        # Create a shadow hand used for calculating Score
    for player, hands in yourHand.items():
        # Splitting is the difficult part
        # You could split the hand,
        # Give the option to double down, It will double their bet and
        # Give them only one more card
        if yourBet[player] == 0:
            continue
        else:
            # if a split is done do it here. have a Dictionary variable called status
            while True:

                print('Player ' + str(player) + ' it is your turn.')
                print('Your Hand: ' + str(hands))
                print('Money: ' + str(yourMoney[player]))
                print('Your Score: ' + str(yourScore[player]))
                ans = ""
                if yourScore[player] > 21:
                    print('You went bust.')
                    break
                elif yourScore[player] == 21:
                    print('You got BlackJack.')
                    break
                elif ans == 'double': # This won't work find something else
                    print('You double downed last turn so your round ends.')
                    break
                else:
                    ans = input(">>> ")
                    if ans == 'h' or ans == 'hit' or ans == 'd' or ans == 'draw':
                        print('You pick up another card')
                        cardInfo = findCardSuit()
                        suit1 = random.choice(cardInfo[0])
                        type1 = random.choice(cardInfo[1])
                        # Find if the index is not in the equation
                        while type1 >= len(deckUsing[suit1]):
                            suit1 = random.choice(cardInfo[0])
                            type1 = random.choice(cardInfo[1])
                        theKey = yourHand[player]
                        theKey.append(deckUsing[suit1][type1])
                        yourHand[player] = theKey
                        shadowHand[player] = theKey

                        deckUsing[suit1].remove(deckUsing[suit1][type1])
                        # Change any none numerical values to numbers
                        for key, value in shadowHand.items():
                            newHand = shadowHand[key]
                            playerScore = 0

                            # this gets the value
                            for i in newHand:
                                cardIndex = newHand.index(i)
                                if i == 'K' or i == 'Q' or i == 'J':
                                    newHand[cardIndex] = 10
                                if i == 'A':
                                    newHand[cardIndex] = 11
                                playerScore += newHand[cardIndex]
                            while playerScore > 21:
                                if 11 in newHand:
                                    handIndex = newHand.index(11)
                                    newHand[handIndex] = 1
                                    playerScore -= 10
                                else:
                                    break
                            shadowHand[key] = newHand
                            yourScore[key] = playerScore
                    elif ans == 'f' or ans == 'fold' or ans == 's' or ans == 'stand':
                        print('You fold and end your turn.')
                        break
                    elif yourMoney[player] >= (2*yourBet[player]):
                        if len(yourHand) == 2:
                            if ans == 'double':
                                print('You double your bet')
                                yourMoney[player] = yourBet[player]
                                yourBet[player] = 2*yourBet[player]

                    else:
                        print('Please insert a valid response.')

        # Now make the scoring part an determine the winner
        total = 0
    # Modify this for the House
    while True:
        print('House Hand: ' + str(hand))
        print("House score: " + str(score))

        print("")
        print("")
        print("")

        time.sleep(1)
        # Now to create the turns. If the AI wants to play a another
        if score > 21:
            print('House went Bust')

            time.sleep(1)
            break
        if score == 21:
            print('House scored BlackJack')
            time.sleep(1)
            break
        if score <= 16:

            print('House Draws')
            cardInfo = findCardSuit()
            suit1 = random.choice(cardInfo[0])
            type1 = random.choice(cardInfo[1])
            # Find if the index is not in the equation
            while type1 >= len(deckUsing[suit1]):
                suit1 = random.choice(cardInfo[0])
                type1 = random.choice(cardInfo[1])
            hand.append(deckUsing[suit1][type1])
            deckUsing[suit1].remove(deckUsing[suit1][type1])

            score = 0

            for x in hand:
                cards = hand.index(x)
                if x == 'K' or x == 'Q' or x == 'J':
                    hand[cards] = 10
                if x == 'A':
                    hand[cards] = 1
                score += hand[cards]

        else:
            print('House Folds')
            break

    for key, value in yourScore.items():
        if yourBet[key] == 0:
            continue
        else:
            if score > 21:
                score = 0
            if value >= score:
                yourLeader[key] = 'Tie'
            if value == 21:
                if len(yourHand) == 2 and len(hand) != 2:
                    yourLeader[key] = 'BigWin'
                elif len(yourHand) == 2 and len(hand) == 2:
                    yourLeader[key] = 'Tie'
                elif len(yourHand) != 2 and len(hand) == 2:
                    yourLeader[key] = 'Lose'
                else:
                    yourLeader[key] = 'MiniWin'
            if value > score:
                yourLeader[key] = 'Won'
            if value > 21:
                yourLeader[key] = 'Lost'
            if value < score:
                yourLeader[key] = 'Lost'
    for key, value in aiScore.items():
        if aiBet[key] == 0:
            continue
        else:
            if score > 21:
                score = 0
            if value == score:
                aiLeader[key] = 'Tie'

            if value == 21 and score == 21:
                if len(aiHand) == 2 and len(hand) != 2:
                    aiLeader[key] = 'BigWin'
                elif len(aiHand) == 2 and len(hand) == 2:
                    aiLeader[key] = 'Tie'
                elif len(aiHand) != 2 and len(hand) == 2:
                    aiLeader[key] = 'Lose'
                else:
                    aiLeader[key] = 'MiniWin'
            if value > score:
                aiLeader[key] = 'Won'
            if value > 21:
                aiLeader[key] = 'Lost'
            if value < score:
                aiLeader[key] = 'Lost'

    for key, value in yourLeader.items():
        if yourBet[key] == 0:
            continue
        else:
            if value == 'Won':
                getWon += 1
                print('Player ' + str(key) + " has won a round")
                yourMoney[key] += yourBet[key] * 1.5
            if value == 'BigWin':
                getWon += 1
                print('Player ' + str(key) + " has won with BlackJack")
                yourMoney[key] += yourBet[key] * 3
            if value == 'MiniWin':
                getWon += 1
                print('Player ' + str(key) + " has won with mini BlackJack")
                yourMoney[key] += yourBet[key] * 2
            if value == 'Tie':
                yourMoney[key] += yourBet[key]
    for key, value in aiLeader.items():
        if aiBet[key] == 0:
            continue
        else:
            if value == 'Won':
                getWon += 1
                print('Ai ' + str(key) + " has won a round")
                aiMoney[key] += aiBet[key] * 1.5
            if value == 'Tie':
                aiMoney[key] += aiBet[key]
            if value == 'BigWin':
                getWon += 1
                print('Player ' + str(key) + " has won with BlackJack")
                aiMoney[key] += aiBet[key] * 3
            if value == 'MiniWin':
                getWon += 1
                print('Player ' + str(key) + " has won with BlackJack")
                aiMoney[key] += aiBet[key] * 2
    if getWon == 0:
        print('The House has won.')

    # Since the AI is the house it will not make or place bets.
    # Looking at black jack rules, if you win against the house you get your money plus some more
    time.sleep(3)
