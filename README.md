# Card Game Simulator

This Python repository simulates a card game environment where you can create cards, decks, and players. The core functionality includes drawing cards, shuffling decks, and managing player hands. 

## Features

- **Card**: Represents a card with a rank and suit.
- **Deck**: Manages a deck of 52 cards, with functionality for drawing and shuffling.
- **Player**: Represents a player with a hand of cards and the ability to draw cards from a deck.
- **Game**: Represents a game with a group of players, where they can draw or pack.
  - **Running mode**:
    - Determines the winner after each round.
    - The game continues for multiple rounds until all rounds are completed.
    - Players can draw or pack cards each round.
  - **Single hand**:
    - Determines the winner after the initial draw for all players at once.
    - The game ends after all players have drawn their cards, and the winner is declared based on their hands.


## Installation

Clone the repository and run the tests to check for functionality.

```bash
git clone https://github.com/Kailashw/card-game-simulator
cd card-game-simulator
```

## Running the game

To run the game, just run following command
```
python main.py
```
