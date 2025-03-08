import random
from models.card import Card

class Deck:
    def __init__(self, include_joker=False):
        """
        Initialize a Deck object with a given set of cards.

        Args:
            include_joker (bool, optional): Include two Jokers in the deck. Defaults to False.
        """
        self.cards = [Card(suit, rank) for suit in Card.suits[:-1] for rank in Card.ranks[:-1]]

        # Add Jokers separately with the correct "None" suit
        if include_joker:
            self.cards.extend([Card("None", "Joker"), Card("None", "Joker")])

    def shuffle(self):
        """
        Shuffle the deck of cards.

        This uses the Fisher-Yates shuffle algorithm to ensure that every possible permutation of cards is equally likely.
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        Draw a single card from the deck.

        Returns:
            Card: The drawn card if the deck is not empty; otherwise, None.
        """
        return self.cards.pop() if self.cards else None

    def add_cards(self, cards: list[Card]):
        """
        Add a list of cards to the deck and shuffle the deck.

        Args:
            cards (list[Card]): A list of Card objects to add to the deck.
        """
        self.cards.extend(cards)
        self.shuffle()

    def draw_multiple(self, num: int):
        """
        Draw multiple cards from the deck.

        Args:
            num (int): The number of cards to draw.

        Returns:
            list[Card] or str: A list of the drawn cards, or an error message if the count is invalid.

        Raises:
            ValueError: If the given count is invalid.
        """
        
        if num <= 0:
            return "Invalid count"
        if num > len(self.cards):
            return "over flow"
        return [self.draw() for _ in range(min(num, len(self.cards)))]
