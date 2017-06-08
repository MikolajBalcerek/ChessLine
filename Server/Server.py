from twisted.internet import reactor, protocol
from twisted.protocols import basic
import time;
import __mainSERVER__;
import Chessgame;

class Server(basic.LineReceiver):
    """This is just about the simplest possible protocol"""

    connectedplayers = 0; #number of connected players overall
    playingplayers = 0; #players currently in games
    matchmakingplayers = 0; #players waiting to be matched for a game
    clients_list = []; #list of all players connected
    waiting_list = []; #list of players waiting to be matched
    games_list = []; #list of all games
    playing_list = [[]]; #list of all players playing in games with ids of games they are in

    def connectionMade(self):
        #what happens when somebody connects
        print (time.strftime("%H:%M") + " New connection made");
        Server.clients_list.append(self);
        Server.connectedplayers = Server.connectedplayers + 1;
        Server.matchmakingplayers = Server.matchmakingplayers + 1;
        self.__helloMessages__()
        self.__messageLIST__(Server.waiting_list, "New player has connected and wants to play!");
        #Server.waiting_list.append(self);
        Server.waiting_list.insert(0, self);
        self.__matchMaking__();


    def __messageLIST__(self, listofusers, text):
        #message privately everyone on the list

        for c in listofusers:
            c.sendLine(text);

    def __helloMessages__(self):
        #a bunch of on-login messages
        self.sendLine("Welcome to Chessline. Author: Mikolaj Balcerek, s416040");
        self.sendLine("Server time: " + time.strftime("%H:%M"));
        self.sendLine("Connected players: " + str(Server.connectedplayers));
        self.sendLine("Available players for matchmaking: " + str(Server.matchmakingplayers));

    def __matchMaking__(self):
        #Find two players on a waiting list and make them play
        # Is there enough players in waiting queue
        if (Server.matchmakingplayers >= 2):

            print (time.strftime("%H:%M") + " Matchmaking two players..");
            #Creating a shortlist of matched players at the moment
            __twoplayers__ = [];
            __twoplayers__.append(Server.waiting_list.pop(0));
            __twoplayers__.append(Server.waiting_list.pop(0));


            #Maintaining numbers of players
            Server.matchmakingplayers = Server.matchmakingplayers - 2;

            #Messaging players that a game has been found
            self.__messageLIST__(__twoplayers__, "Found a pair.. Connecting");

            self.__makeGame__(__twoplayers__);
        else:
            #Not enough players, you have to wait!
            self.sendLine("Please wait to be matched with another player");


    def __makeGame__(self, __twoplayers__):
        #Makes the game given list of any free two players

        #Maintaining numbers
        Server.playingplayers = Server.playingplayers + 2;

        # Sending over the command codes to initialize game modes on clients
        self.clearLineBuffer();
        self.__messageLIST__(__twoplayers__, "GAMEMODE");

        # Server logs and figuring out game's id
        idnumber = len(Server.games_list);
        print (time.strftime("%H:%M") + " Hosted a game. ID = " + str(idnumber));

        # Adding players to playing players list with the game's id
        Server.playing_list.append([__twoplayers__[0] , idnumber]);
        Server.playing_list.append([__twoplayers__[1], idnumber]);

        #running the game
        Server.games_list.append(Chessgame.Chessgame(self, __twoplayers__, idnumber));



    def connectionLost(self, reason):
        #Handling dropped connections

        #Maintaining numbers and lists of ALL connected players
        Server.connectedplayers = Server.connectedplayers - 1;
        Server.clients_list.remove(self);

        #Disconnected player was in a waiting list
        if (self in Server.waiting_list):
            Server.waiting_list.remove(self);
            Server.matchmakingplayers = Server.matchmakingplayers - 1;

        #Disconnected player was in a game, checking
        for playerandgame in Server.playing_list:
            if (self in playerandgame):
                print ("Player in a chess game has disconnected");
                gameid = playerandgame[1];
                thegame = Server.games_list[gameid]
                #inform the game
                thegame.playerDisconnected(self);
                #if player is still on the list
                try:
                    Server.playing_list.remove([self, gameid]);
                except ValueError:
                    #player was already removed
                    pass;

        print ("Connection Lost and handled by the server");


    def lineReceived(self, line):
        #we got something from a client
        print (time.strftime("%H:%M ") + "Received a message: " + str(line));

        #is the client playing in a game
        if (any(self in sublist for sublist in Server.playing_list)):

            # find the game's id
            for playerandgame in Server.playing_list:
                if(self in playerandgame):
                    gameid = playerandgame[1];
                    thegame = Server.games_list[gameid];

            #is it the player's turn and the game hasn't ended
            if (self == thegame.players[thegame.playerturn] and (thegame.gameover == False)):
                #was the message legit
                if(thegame.getmessage(line, self)):
                    print (time.strftime("%H:%M") + " Legit command was received and processed");
                    #Engange the next turn function
                    thegame.__AfterMove__();

                else:
                    #the message was somehow incorrect, sending special client side code to try again
                    list = [];
                    list.append(self);
                    self.__messageLIST__(list, "TRYAGAIN");

        #the client is in the lobby but after having played the game
        elif (str(line) == "MATCH") and not (self in Server.waiting_list):
            Server.waiting_list.append(self);
            Server.matchmakingplayers = Server.matchmakingplayers + 1;
            Server.__matchMaking__(self);



    #def dataReceived(self, data):
    #    "As soon as any data is received, write it back."
     #   self.transport.write("Welcome to Chessline. Mikolaj Balcerek, s416040");
     #   print ("Server time: " +  time.strftime("%H:%M"));