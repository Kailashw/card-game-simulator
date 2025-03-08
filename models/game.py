from collections import Counter
from models.card import Card
from models.player import Player
from models.deck import Deck
import pprint

class Game:
    def __init__(self, player_names: list[str], include_joker=False):
        self.deck = Deck(include_joker=include_joker)
        self.deck.shuffle()
        self.players = {name: Player(name) for name in player_names}

    def deal(self, num_cards: int):
        for _ in range(num_cards):
            for player in self.players.values():
                player.draw(self.deck)

    def show_hands(self):
        hands = {player.name: player.show_hand() for player in self.players.values()}
        pprint.pprint(hands)

    def remove_player(self, player_name: str):
        if player_name in self.players:
            self.deck.add_cards(self.players[player_name].hand)
            del self.players[player_name]

    def evaluate_hand(self, hand):
        """Determine the ranking of a given hand, considering Joker only when necessary."""
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
