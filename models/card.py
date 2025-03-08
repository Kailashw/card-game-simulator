class Card:
    suits = ["♣", "♦", "♥", "♠", "None"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "Joker"]
    rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, suit: str, rank: str):
        if suit not in Card.suits or rank not in Card.ranks:
            raise ValueError("invalid suit or rank")

        self.suit = suit
        self.rank = rank

    def __repr__(self):
        # Special case: If the card is a Joker, display only "Joker"
        if self.rank == "Joker":
            return "Joker"
        return f'{self.rank}{self.suit}'

    def __eq__(self, other):
        return Card.suits.index(self.suit) == Card.suits.index(other.suit) and Card.rank_values[self.rank] == Card.rank_values[other.rank]

    def __lt__(self, other):
        suitScoreLesser = Card.suits.index(self.suit) < Card.suits.index(other.suit)
        suitScoreEqual = Card.suits.index(self.suit) == Card.suits.index(other.suit)
        return True if suitScoreLesser or (suitScoreEqual and Card.rank_values[self.rank] < Card.rank_values[other.rank]) else False
    
    def __gt__(self, other): 
        suitScoreGreater = Card.suits.index(self.suit) > Card.suits.index(other.suit)
        suitScoreEqual = Card.suits.index(self.suit) == Card.suits.index(other.suit)
        return True if suitScoreGreater or (suitScoreEqual and Card.rank_values[self.rank] > Card.rank_values[other.rank]) else False
