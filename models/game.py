from collections import Counter
from models.card import Card
from models.player import Player
from models.deck import Deck
import pprint

class Game:
    def __init__(self, player_names: list[str], include_joker=False):
        """
        Initialize a Game object with a given set of players.

        Args:
            player_names (list[str]): A list of player names.
            include_joker (bool, optional): Include two Jokers in the deck. Defaults to False.
        """
        self.deck = Deck(include_joker=include_joker)
        self.deck.shuffle()
        self.players = {name: Player(name) for name in player_names}

    def deal(self, num_cards: int):
        """
        Deal a specified number of cards to each player in the game.

        Args:
            num_cards (int): The number of cards to deal to each player.

        Returns:
            None
        """
        
        for _ in range(num_cards):
            for player in self.players.values():
                player.draw(self.deck)

    def show_hands(self):
        """
        Display the current hands of all players in the game.

        Retrieves each player's hand and prints it in a readable format using
        pretty print.

        No arguments are required, and the function does not return any values.
        """
        hands = {player.name: player.show_hand() for player in self.players.values()}
        pprint.pprint(hands)

    def remove_player(self, player_name: str):
        """
        Remove a player from the game by their name.

        If the player exists, their hand is returned to the deck, and the player is removed from the game.

        Args:
            player_name (str): The name of the player to remove.
        """
        if player_name in self.players:
            self.deck.add_cards(self.players[player_name].hand)
            del self.players[player_name]

    def evaluate_hand(self, hand):
        """
        Evaluate the given hand of cards and return a tuple of (hand_name, values) where
        hand_name is a string describing the type of hand (e.g. "Straight Flush", "One Pair", etc.)
        and values is a list of integers representing the ranks of the cards in the hand.

        The order of the ranks in the list is important for determining the best hand in case of a tie.
        The first element in the list is the highest ranking card, the second element is the second highest, etc.

        If the hand contains a Joker, it is used to complete a Straight or other combinations if possible.
        If the Joker is not used, it is not included in the list of ranks.

        The possible hand names and the corresponding values are as follows:

        - Straight Flush: A list of 5 consecutive ranks in the same suit, e.g. [3, 4, 5, 6, 7]
        - Four of a Kind: A list of 4 identical ranks, followed by the highest ranking kicker, e.g. [4, 4, 4, 4, 8]
        - Full House: A list of 3 identical ranks, followed by a pair of identical ranks, e.g. [3, 3, 3, 7, 7]
        - Flush: A list of 5 ranks in the same suit, e.g. [2, 3, 5, 6, 9]
        - Straight: A list of 5 consecutive ranks, e.g. [3, 4, 5, 6, 7]
        - Three of a Kind: A list of 3 identical ranks, followed by the two highest ranking kickers, e.g. [3, 3, 3, 9, 7]
        - Two Pair: A list of 2 identical ranks, followed by a second pair of identical ranks, followed by the highest ranking kicker, e.g. [2, 2, 5, 5, 9]
        - One Pair: A list of 2 identical ranks, followed by the three highest ranking kickers, e.g. [2, 2, 9, 7, 5]
        - High Card: A list of the highest ranking cards, e.g. [9, 7, 5, 3, 2]

        """
        if not hand:
            return ("No Cards", [])
        
        # Separate out Joker and non-Joker cards
        non_joker_cards = [card for card in hand if card.rank != "Joker"]
        joker_count = sum(1 for card in hand if card.rank == "Joker")
        
        ranks = [card.rank for card in non_joker_cards]
        suits = [card.suit for card in non_joker_cards]
        rank_counts = Counter(ranks)
        unique_ranks = sorted([Card.rank_values[r] for r in ranks])
        
        is_flush = len(set(suits)) == 1
        is_straight = all(unique_ranks[i] + 1 == unique_ranks[i + 1] for i in range(len(unique_ranks) - 1))
        
        # Handle Joker used for completing a Straight or other combinations
        if joker_count > 0:
            # Try to form a Straight by adding the Joker if possible
            if not is_straight:  # If it's not already a straight
                # Sort the unique ranks
                unique_ranks = sorted([Card.rank_values[r] for r in ranks])
                
                # Look for gaps in the sequence
                for i in range(1, len(unique_ranks)):
                    if unique_ranks[i] != unique_ranks[i-1] + 1:
                        # If there's a gap, use the Joker to complete the sequence
                        # The Joker can fill the gap by assuming the missing rank
                        missing_rank = unique_ranks[i-1] + 1
                        unique_ranks.append(missing_rank)
                        unique_ranks.sort()
                        break  # Joker has been used, no need to continue

                # Re-check if the hand forms a straight after the modification
                is_straight = all(unique_ranks[i] + 1 == unique_ranks[i + 1] for i in range(len(unique_ranks) - 1))

        # Now handle hand evaluations based on the updated ranks
        if is_flush and is_straight:
            return ("Straight Flush", unique_ranks)
        elif 4 in rank_counts.values():
            four_kind = [rank for rank, count in rank_counts.items() if count == 4]
            kicker = sorted([Card.rank_values[rank] for rank in ranks if rank != four_kind[0]], reverse=True)
            return ("Four of a Kind", [Card.rank_values[four_kind[0]]] + kicker)
        elif 3 in rank_counts.values() and 2 in rank_counts.values():
            three_kind = [rank for rank, count in rank_counts.items() if count == 3]
            pair = [rank for rank, count in rank_counts.items() if count == 2]
            return ("Full House", [Card.rank_values[three_kind[0]], Card.rank_values[pair[0]]])
        elif is_flush:
            return ("Flush", sorted(unique_ranks, reverse=True))
        elif is_straight:
            return ("Straight", unique_ranks)
        elif 3 in rank_counts.values():
            three_kind = [rank for rank, count in rank_counts.items() if count == 3]
            kicker = sorted([Card.rank_values[rank] for rank in ranks if rank != three_kind[0]], reverse=True)
            return ("Three of a Kind", [Card.rank_values[three_kind[0]]] + kicker)
        elif list(rank_counts.values()).count(2) == 2:
            pairs = sorted([Card.rank_values[rank] for rank, count in rank_counts.items() if count == 2], reverse=True)
            kicker = sorted([Card.rank_values[rank] for rank in ranks if rank not in pairs], reverse=True)
            return ("Two Pair", pairs + kicker)
        elif 2 in rank_counts.values():
            pair = [rank for rank, count in rank_counts.items() if count == 2]
            kicker = sorted([Card.rank_values[rank] for rank in ranks if rank != pair[0]], reverse=True)
            return ("One Pair", [Card.rank_values[pair[0]]] + kicker)
        else:
            return ("High Card", sorted([Card.rank_values[rank] for rank in ranks], reverse=True))


    def determine_winner(self):
        """Determine the player with the best hand."""
        hand_rankings = {
            "Straight Flush": 8,
            "Four of a Kind": 7,
            "Full House": 6,
            "Flush": 5,
            "Straight": 4,
            "Three of a Kind": 3,
            "Two Pair": 2,
            "One Pair": 1,
            "High Card": 0,
            "Wildcard Hand": 9  # Joker cases get the highest priority
        }

        best_hand = None
        best_player = None
        best_hand_value = None

        for player in self.players.values():
            hand_type, hand_value = self.evaluate_hand(player.hand)
            print(f"{player.name} has {hand_type} with value {hand_value}")

            if best_hand is None or hand_rankings[hand_type] > hand_rankings[best_hand]:
                best_hand = hand_type
                best_player = player.name
                best_hand_value = hand_value
            elif hand_rankings[hand_type] == hand_rankings[best_hand]:
                # If hands are the same type, break the tie by comparing hand values
                if hand_value > best_hand_value:
                    best_hand = hand_type
                    best_player = player.name
                    best_hand_value = hand_value
        
        return best_player, best_hand
