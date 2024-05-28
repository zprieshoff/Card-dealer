#Zechariah Prieshoff
#Card Dealer
#May 21st, 2024
#Program outputs the framework for a basic card game. It uses a standard 52-card deck
#and assigns random cards to the player and the computer.

""" cards.py
    demonstrates functions
    manage a deck of cards db
"""

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

import random

print("Welcome to the Python Card Dealer! \n===================================")

def initializeDeck():
    return [DECK] * NUMCARDS

def dealCards(database, hand):
    cardsAvailable = [i for i in range(NUMCARDS) if database[i] == DECK]
    if cardsAvailable:
        card = random.choice(cardsAvailable)
        database[card] = hand
        
def showHand(database, hand):
    handName = HANDS[hand]
    for i in range(NUMCARDS):
        if database[i] == hand:
            rank = RANKNAME[i % 13]
            suit = SUITNAME[i // 13]
            print(f"{rank} of {suit}")
            
def showDeck(database):
    for i in range(NUMCARDS):
        rank = RANKNAME[i % 13]
        suit = SUITNAME[i // 13]
        hand = HANDS[database[i]]
        print(f"{i:>2}) {rank} of {suit:<9} {hand}")
            
def main():
    database = initializeDeck()
    for i in range(5):
        dealCards(database, PLAYER)
        dealCards(database, COMPUTER)
    
    hands = input("Are you ready to see your and the computers hands? (yes/no):  ").lower()
    
    if hands == 'yes':
        print("\nHere's the deck!\n===================================")
        showDeck(database)
        print("\nHere is your hand!\n")
        showHand(database, PLAYER)
        print("\nHere is the computers hand!\n")
        showHand(database, COMPUTER)
    elif hands == 'no':
        print("Okay, see you later!")
    else:
        print("Sorry, invalid input.")

if __name__ == "__main__":
    main()