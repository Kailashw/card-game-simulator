
from models.deck import Deck

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return self.name

    def draw(self, deck=Deck):
        card = deck.draw()
        return self.hand.append(card) if card else card
    
    def draw_multiple(self, deck=Deck, card_count=int):
        cards = deck.draw_multiple(card_count)
        return self.hand.extend(cards) if len(cards) else cards
    
    def show_hand(self):
        return self.hand
    
    def card_sort(self):
        # Define the order of suits and ranks
        suit_order = {"♣": 0, "♦": 1, "♥": 2, "♠": 3}
        rank_order = {str(i): i for i in range(2, 11)}
        rank_order.update({"J": 11, "Q": 12, "K": 13, "A": 14})

        def sort_key(card):
            rank, suit = card[:-1], card[-1]  # Split the rank and suit
            return (suit_order[suit], rank_order[rank])

        # Sort the cards using the custom key
        return sorted(self.hand, key=sort_key)
  