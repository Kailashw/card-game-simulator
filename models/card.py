class Card:
    suits = ["♣", "♦", "♥", "♠", "None"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "Joker"]
    rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, suit: str, rank: str):
        """
        Initialize a Card object with a given suit and rank.

        Args:
            suit (str): The suit of the card. Must be one of the following:
                - "♣" (clubs)
                - "♦" (diamonds)
                - "♥" (hearts)
                - "♠" (spades)
                - "None" (no suit, i.e. Joker)
            rank (str): The rank of the card. Must be one of the following:
                - "2", "3", ..., "10"
                - "J", "Q", "K", "A"
                - "Joker"

        Raises:
            ValueError: If the given suit or rank is invalid.
        """
        if suit not in Card.suits or rank not in Card.ranks:
            raise ValueError("invalid suit or rank")

        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """
        Return a string representation of the card.

        If the card is a Joker, return the string "Joker". Otherwise, return a string
        in the format "<rank><suit>", e.g. "K♠" or "Q♦".
        """
        if self.rank == "Joker":
            return "Joker"
        return f'{self.rank}{self.suit}'

    def __eq__(self, other):
        """
        Return True if the given card is equal to this card, False otherwise.

        Two cards are equal if and only if they have the same suit and rank.
        """
        return Card.suits.index(self.suit) == Card.suits.index(other.suit) and Card.rank_values[self.rank] == Card.rank_values[other.rank]

    def __lt__(self, other):
        """
        Return True if this card is less than the given card, False otherwise.

        A card is considered less than another if its suit is less than the other's suit, or
        if its suit is equal to the other's suit and its rank is less than the other's rank.
        """
        suitScoreLesser = Card.suits.index(self.suit) < Card.suits.index(other.suit)
        suitScoreEqual = Card.suits.index(self.suit) == Card.suits.index(other.suit)
        return True if suitScoreLesser or (suitScoreEqual and Card.rank_values[self.rank] < Card.rank_values[other.rank]) else False
    
    def __gt__(self, other): 
        """
        Return True if this card is greater than the given card, False otherwise.

        A card is considered greater than another if its suit is greater than the other's suit, or
        if its suit is equal to the other's suit and its rank is greater than the other's rank.
        """
        suitScoreGreater = Card.suits.index(self.suit) > Card.suits.index(other.suit)
        suitScoreEqual = Card.suits.index(self.suit) == Card.suits.index(other.suit)
        return True if suitScoreGreater or (suitScoreEqual and Card.rank_values[self.rank] > Card.rank_values[other.rank]) else False
