from models.game import Game

if __name__ == "__main__":
    game = Game(["Dean", "Alice", "Bob", "Charlie", "Kailash"], include_joker=True)
    game.deal(3)
    game.show_hands()

    print("\nCharlie drops out of the game.")
    game.remove_player("Charlie")
    game.show_hands()

    winner, best_hand = game.determine_winner()
    print(f"\nWinner: {winner} with a {best_hand}")
