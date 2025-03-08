
from models.deck import Deck

class Player:
    def __init__(self,name):
        """
        Initialize a Player object with a given name.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.hand = []

    def __repr__(self):
        """
        Return a string representation of the player.

        Returns:
            str: The player's name.
        """

        return self.name

    def draw(self, deck=Deck):
        """
        Draw a single card from the deck and add it to the player's hand.

        Args:
            deck (Deck, optional): The deck to draw from. Defaults to a new Deck().

        Returns:
            Card or None: The drawn card if successful, otherwise None if the deck is empty.
        """
        card = deck.draw()
        return self.hand.append(card) if card else card
    
    def draw_multiple(self, deck=Deck, card_count=int):
        """
        Draw multiple cards from the deck and add them to the player's hand.

        Args:
            deck (Deck, optional): The deck to draw from. Defaults to a new Deck().
            card_count (int, optional): The number of cards to draw. Defaults to 1.

        Returns:
            list[Card] or str: A list of the drawn cards if the count is valid, otherwise an error message.
        """
        cards = deck.draw_multiple(card_count)
        return self.hand.extend(cards) if len(cards) else cards
    
    def show_hand(self):
        """
        Display the player's current hand of cards.

        Returns:
            list[Card]: A list of Card objects representing the player's hand.
        """
        return self.hand
    
    def card_sort(self):
        """
        Sort the player's hand of cards in ascending order based on suit and rank.

        The sorting is done first by suit in the order of clubs, diamonds, hearts, and spades,
        and then by rank within each suit from 2 to 10, followed by J, Q, K, and A.

        Returns:
            list[Card]: A list of Card objects sorted by suit and rank.
        """

        suit_order = {"♣": 0, "♦": 1, "♥": 2, "♠": 3}
        rank_order = {str(i): i for i in range(2, 11)}
        rank_order.update({"J": 11, "Q": 12, "K": 13, "A": 14})

        def sort_key(card):
            rank, suit = card[:-1], card[-1]  # Split the rank and suit
            return (suit_order[suit], rank_order[rank])

        # Sort the cards using the custom key
        return sorted(self.hand, key=sort_key)
  