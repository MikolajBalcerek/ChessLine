# Chessline
Chess Server and Client implementation based on Twisted + python-chess
Python 2.7+
Written for Computer Networks course, 2016/2017
Author: Mikołaj Balcerek, s416040

## Features
- Play many games simultaneously
- Lobby for awaiting players
- Handling disconnects at any stage
- Matching pairs of players automatically
- Play chess using long algebraic notation ("e2e4")
- Move validation
- Draws, stalemates and other game-ending conditions (e.g. insufficient material)
- Forfeiting (type: FORFEIT)
- Player and games counts (players in games and awaiting for a match)

## Unfinished
- Returning players to the lobby after the game has finished
- Chatting
