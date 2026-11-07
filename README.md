# Connect Four (Puissance 4)

Connect Four in Python and Tkinter: play against a friend or against a computer opponent driven by minimax with alpha-beta pruning.

## How it works
- Standard 7-column, 6-row board. Click a column to drop a disc. The first to line up 4 discs horizontally, vertically or diagonally wins.
- **Minimax with alpha-beta pruning**: for each playable column, the computer simulates the move and searches the game tree, keeping the column with the best score.
- **Adaptive depth**: the search depth grows with the number of full columns. As the board fills and fewer moves are possible, it looks further ahead at a similar cost.
- **Scoring**: a win scores 100 plus a bonus for how early it happens, a loss the opposite, a full board or an unfinished position 0. The AI prefers quick wins and delays losses.
- **Fast win check**: only the lines through the disc just played are checked, not the whole board.
- On equal scores it prefers the centre column.

## Tech stack
Python 3, Tkinter (standard library only).

## Run it locally
```bash
python main.py
```
Choose **Contre un ami** or **Contre l'ordi**, then click a column. You play first.

## Context
Personal project, October to November 2022. Minimax came first; alpha-beta pruning was added later to make deeper searches fast enough.
