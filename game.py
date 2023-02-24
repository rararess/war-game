from random import shuffle
import time

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    def __init__(self):
        print("Creating new ordered deck!")
        time.sleep(0.5)
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        time.sleep(0.5)
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0

print("Welcome to War!")
time.sleep(0.5)

# Creating a new deck and splitting it in half:

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# Creating players

name1 = input("Insert name for player 1: ")
name2 = input("Insert name for player 2: ")

player1 = Player(name1, Hand(half1))
player2 = Player(name2, Hand(half2))

total_rounds = 0
war_count = 0

while player1.still_has_cards() and player2.still_has_cards():
    total_rounds += 1
    print("\nNew Round")
    print("The current standings: ")
    print(player1.name + " has the count: " + str(len(player1.hand.cards)))
    print(player2.name + " has the count: " + str(len(player2.hand.cards)))
    print("Play a card!")
    print('\n')

    table_cards = []

    p1_card = player1.play_card()
    p2_card = player2.play_card()

    table_cards.append(p1_card)
    table_cards.append(p2_card)

    if p1_card[1] == p2_card[1]:
        war_count += 1

        print("WAR!!!")

        table_cards.extend(player1.remove_war_cards())
        table_cards.extend(player2.remove_war_cards())

        if RANKS.index(p1_card[1]) < RANKS.index(p2_card[1]):
            player2.hand.add(table_cards)
        else:
            player1.hand.add(table_cards)

    else:
        if RANKS.index(p1_card[1]) < RANKS.index(p2_card[1]):
            player2.hand.add(table_cards)
        else:
            player1.hand.add(table_cards)

time.sleep(0.5)
print("\nGame over!\nNumber of rounds: " + str(total_rounds) + "\nA war happened " + str(war_count) + " times")
time.sleep(0.5)
print("Does {} has cards? ".format(player1.name))
print(str(player1.still_has_cards()))
time.sleep(0.5)
print("Does {} has cards? ".format(player2.name))
print(str(player2.still_has_cards()))

#

