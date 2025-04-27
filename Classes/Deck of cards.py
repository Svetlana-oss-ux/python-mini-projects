# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 02:47:47 2025

@author: SEA4720
"""

import random

# =========================================
# Class representing a single Card
# =========================================
class Card:
    valid_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    valid_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, value):
        self._suit = None
        self._value = None
        self.suit = suit    # Use setter for validation
        self.value = value  # Use setter for validation

    # Getter for suit
    @property
    def suit(self):
        return self._suit

    # Setter for suit with validation
    @suit.setter
    def suit(self, suit):
        if suit not in Card.valid_suits:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {Card.valid_suits}.")
        self._suit = suit

    # Getter for value
    @property
    def value(self):
        return self._value

    # Setter for value with validation
    @value.setter
    def value(self, value):
        if value not in Card.valid_values:
            raise ValueError(f"Invalid value: {value}. Must be one of {Card.valid_values}.")
        self._value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

# =========================================
# Class representing a full deck of 52 cards
# =========================================
class DeckOfCard:
    def __init__(self):
        self.deck = [Card(suit, value) for suit in Card.valid_suits for value in Card.valid_values]

    def shuffle(self):
        random.shuffle(self.deck)
        print("Deck has been shuffled.")

    def deal(self):
        if not self.deck:
            print("No more cards left in the deck!")
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        print(f"Dealt card: {card}")
        return card

    def __str__(self):
        return f"Deck of {len(self.deck)} cards."

# =========================================
# Example of usage
# =========================================
if __name__ == "__main__":
    deck = DeckOfCard()
    print(deck)

    deck.shuffle()
    deck.deal()
    deck.deal()

    print(deck)
