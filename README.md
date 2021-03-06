# Chessline
Chess Server and Client implementation based on Twisted + python-chess  
Python 2.7+  
Written for Computer Networks course, 2016/2017  
Author: Mikołaj Balcerek, s416040  
Version: 0.3, mostly stable
++Veteran players can abstain from further matchmaking

## Features

- Play many games simultaneously
- Lobby for awaiting players
- Handling disconnects at any stage
- Matching pairs of players automatically
- Play chess using long algebraic notation ("e2e4")
- Returning players to the lobby after the game has finished and shuffling (new players have priority to play)
- Veteran players can choose to avoid further automatic matchmaking (type in MATCH or answer yes after your game has ended)
- Move and validation
- Draws, stalemates and other game-ending conditions (e.g. insufficient material)
- Forfeiting (type: FORFEIT)
- Player and games counts (players in games and awaiting for a match)
- Choose addresses and ports used (SetupTalk classes)

## Example
```
23:46 Server: Welcome to Chessline. Author: Mikolaj Balcerek, s416040
23:46 Server: Server time: 23:46
23:46 Server: Connected players: 2
23:46 Server: Available players for matchmaking: 2
23:46 Server: Found a pair.. Connecting
-------------------------------------------------------
23:46 You: Type FORFEIT to surrender
23:46 You: Type moves in UCI, long algebraic notation, e.g e2e4
23:46 Server:
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
23:46 You: It's time for you to make a move or issue a command!
Your command: FORFEIT
23:46 You: Sent!
23:46 You: You have forfeited the game
23:46 Server: You have been put in the matchmaking lobby again but won't be able to play the same opponent.
23:46 You: Do you want join the waiting queue and force matchmaking immediately (allow for repeat opponents)?
Yes
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
9. Type MATCH or answer yes to mark yourself as ready for the next game.
## Unfinished and known bugs
-

