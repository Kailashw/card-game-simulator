from models.card import Card

def test_card_initialization():
    # Test valid card creation
    card1 = Card("♠", "A")
    card2 = Card("♥", "10")
    card3 = Card("♦", "3")
    
    assert card1.suit == "♠" and card1.rank == "A"
    assert card2.suit == "♥" and card2.rank == "10"
    assert card3.suit == "♦" and card3.rank == "3"
    
    # Test invalid card creation (raises ValueError)
    try:
        Card("♣", "1")  # Invalid rank
    except ValueError as e:
        assert str(e) == "invalid suit or rank"
    
    try:
        Card("♢", "A")  # Invalid suit
    except ValueError as e:
        assert str(e) == "invalid suit or rank"

def test_card_repr():
    # Test the string representation of the card
    card = Card("♠", "A")
    assert repr(card) == "A♠"
    
    card = Card("♦", "10")
    assert repr(card) == "10♦"

def test_card_comparisons():
    # Test equality comparison using __eq__
    card1 = Card("♠", "A")
    card2 = Card("♠", "A")
    card3 = Card("♠", "K")
    card4 = Card("♥", "A")
    
    assert card1 == card2  # Same suit and rank (use __eq__)
    assert card1 != card3  # Different rank (same suit) (use __ne__)
    assert card1 != card4  # Different suit (same rank) (use __ne__)

    # Test less than comparison using __lt__
    card1 = Card("♠", "9")
    card2 = Card("♠", "10")
    card3 = Card("♦", "3")
    card4 = Card("♥", "K")
    
    assert card1 < card2  # Same suit, lower rank (use __lt__)
    assert card2 > card1  # Same suit, higher rank (use __gt__)
    assert not card1 < card3  # Different suits, ♠ < ♦ (use __lt__)
    assert card3 < card4  # Different suits, ♦ < ♥ (use __lt__)
    
    # Test greater than comparison using __gt__
    card5 = Card("♠", "2")
    card6 = Card("♣", "A")
    
    assert card5 > card6  # ♠ > ♣ (due to suit order) (use __gt__)
    
    card7 = Card("♦", "A")
    card8 = Card("♦", "K")
    assert not card7 < card8  # A < K (same suit) (use __lt__)

def test_card_sort():
    # Test sorting of a list of cards
    cards = [
        Card("♠", "A"),
        Card("♣", "3"),
        Card("♦", "10"),
        Card("♥", "K"),
        Card("♠", "2")
    ]
    
    sorted_cards = sorted(cards)
    
    # Expected sorted order by suit then rank
    expected_order = [
        Card("♣", "3"),
        Card("♦", "10"),
        Card("♥", "K"),
        Card("♠", "2"),
        Card("♠", "A")
    ]
    
    for i, card in enumerate(sorted_cards):
        assert repr(card) == repr(expected_order[i])

def run_tests():
    test_card_initialization()
    test_card_repr()
    test_card_comparisons()
    test_card_sort()
    print("All tests passed!")

# Run the tests
run_tests()
