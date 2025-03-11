from models.game import Game
from models.task_scheduler import TaskScheduler

if __name__ == "__main__":
    print("Starting Game 1 !! Determining winner in list of Cards.")
    game = Game(["Dean", "Alice", "Bob", "Charlie", "Kailash"], include_joker=True)
    game.deal(3)
    game.show_hands()
    print("\nCharlie drops out of the game.")
    game.remove_player("Charlie")
    game.show_hands()
    winner, best_hand = game.determine_winner()
    print(f"\nWinner: {winner} with a {best_hand}")
    print("End of Game 1!! Determining Winner in running hand in each round.")
    print("Starting Game 2!!")
    game = Game(["Dean", "Alice", "Bob", "Charlie"])
    game.play_game()
    print("End of Game 2!!")
