from models.card import Card
from models.deck import Deck

def test_deck_initialization(self):
    # Initialize deck and check it contains 52 cards
    deck = Deck()
    self.assertEqual(len(deck.cards), 52)
    self.assertTrue(all(isinstance(card, Card) for card in deck.cards))

def test_draw_single_card(self):
    deck = Deck()
    # Initially, the deck should have 52 cards
    self.assertEqual(len(deck.cards), 52)
    
    drawn_card = deck.draw()
    # The drawn card should be a string and one card should be removed
    self.assertIsInstance(drawn_card, str)
    self.assertEqual(len(deck.cards), 51)

def test_draw_multiple_cards(self):
    deck = Deck()
    # Draw 5 cards
    drawn_cards = deck.draw_multiple(5)
    # Ensure 5 cards are drawn and returned
    self.assertEqual(len(drawn_cards), 5)
    # Ensure all cards are strings
    self.assertTrue(all(isinstance(card, str) for card in drawn_cards))
    # The deck should have 47 cards after drawing 5
    self.assertEqual(len(deck.cards), 47)

def test_draw_more_than_available_cards(self):
    deck = Deck()
    # Draw all 52 cards
    for _ in range(52):
        deck.draw()
    # Try drawing one more card from the empty deck
    self.assertIsNone(deck.draw())

def test_shuffle_deck(self):
    deck = Deck()
    initial_order = deck.cards[:]
    # Shuffle the deck
    deck.shuffle()
    # Check if the deck order has changed (it should be different)
    self.assertNotEqual(initial_order, deck.cards)

def test_draw_multiple_from_empty_deck(self):
    deck = Deck()
    # Draw all 52 cards first
    deck.draw_multiple(52)
    # Draw 5 cards from the empty deck
    drawn_cards = deck.draw_multiple(5)
    self.assertEqual(len(drawn_cards), 0)  # No cards should be drawn
    self.assertEqual(len(deck.cards), 0)  # Deck should be empty

def test_deck_integrity_after_draw_multiple(self):
    deck = Deck()
    # Draw 10 cards
    drawn_cards = deck.draw_multiple(10)
    self.assertEqual(len(drawn_cards), 10)
    self.assertEqual(len(deck.cards), 42)  # 52 - 10 = 42 cards remaining

def test_draw_multiple_invalid_count(self):
    deck = Deck()
    # Try drawing more than the available cards
    drawn_cards = deck.draw_multiple(100)
    self.assertEqual(len(drawn_cards), 52)  # All 52 cards should be drawn
    self.assertEqual(len(deck.cards), 0)  # Deck should be empty

