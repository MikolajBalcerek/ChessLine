# Chessline
Chess Server and Client implementation based on Twisted + python-chess  
Python 2.7+  
Written for Computer Networks course, 2016/2017  
Author: Mikołaj Balcerek, s416040
Version: 0.2, mostly stable  
++returning to lobby and shuffling

## Features

- Play many games simultaneously
- Lobby for awaiting players
- Handling disconnects at any stage
- Matching pairs of players automatically
- Play chess using long algebraic notation ("e2e4")
- Returning players to the lobby after the game has finished and shuffling so there are mostly no repeat games (new players have priority to play)
- Move and validation
- Draws, stalemates and other game-ending conditions (e.g. insufficient material)
- Forfeiting (type: FORFEIT)
- Player and games counts (players in games and awaiting for a match)
- Choose addresses and ports used (SetupTalk classes)

## Example
```
21:39 Server: Welcome to Chessline. Author: Mikolaj Balcerek, s416040
21:39 Server: Server time: 21:39
21:39 Server: Connected players: 3
21:39 Server: Available players for matchmaking: 1
21:39 Server: Please wait to be matched with another player
21:40 Server: New player has connected and wants to play!
21:40 Server: Found a pair.. Connecting
-------------------------------------------------------
21:40 You: Type FORFEIT to surrender
21:40 You: Type moves in UCI, long algebraic notation, e.g e2e4
21:40 Server:
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
21:40 You: It's time for you to make a move or issue a command!
Your command: FORFEIT
```

### Running Chessline
1. Make sure you have Python 2.7+, Twisted and python-chess installed
2. Run Chessline/Server/\_\_mainSERVER\_\_.py
3. Answer prompts (Write down that port number!)
4. Run Chessline/Client/\_\_mainCLIENT\_\__.py
5. Answer prompts (localhost for 127.0.0.1 or any valid ipv4, the port number from 3.)
6. Repeat steps 4-5 as many times as you wish
7. Wait to be automatically matched
8. Play chess using long algebraic notation ("e2e4") or type "FORFEIT" to give up

## Unfinished and known bugs
- Waiting players count gets messed up after series of disconnects and returns to the lobby, however the matchmaking functionality still persists

