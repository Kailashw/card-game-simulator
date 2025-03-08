import random
from models.card import Card

class Deck:
    def __init__(self, include_joker=False):
        # Create a standard deck (excluding "None" suit)
        self.cards = [Card(suit, rank) for suit in Card.suits[:-1] for rank in Card.ranks[:-1]]

        # Add Jokers separately with the correct "None" suit
        if include_joker:
            self.cards.extend([Card("None", "Joker"), Card("None", "Joker")])

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

    def add_cards(self, cards: list[Card]):
        self.cards.extend(cards)
        self.shuffle()

    def draw_multiple(self, num: int):
        if num <= 0:
            return "Invalid count"
        if num > len(self.cards):
            return "over flow"
        return [self.draw() for _ in range(min(num, len(self.cards)))]
