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
        Server.matchmakingplayers = Server.connectedplayers - Server.playingplayers;
        self.__helloMessages__()
        self.__messageLIST__(Server.waiting_list, "New player has connected and wants to play!");
        Server.waiting_list.append(self);
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
        self.playing_list.append([__twoplayers__[0] , idnumber]);
        self.playing_list.append([__twoplayers__[1], idnumber]);

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

        #Disconnected player was in a game
        if (self in self.playing_list):
            #find the game's id
            index = self.playing_list.index(self);
            gameid = self.playing_list[index][0];

            #inform the game
            #self.games_list[index].forfeit

            #remove the player from players' list
            Server.playing_list.remove(self);

        print ("Connection Lost");


    def lineReceived(self, line):
        #we got something from a client

        #is the client playing in a game
        if (self in self.playing_list):
            # find the game's id
            index = self.playing_list.index(self);
            gameid = self.playing_list[index][0];
            thegame = self.games_list[gameid];

            #is it the player's turn
            if (self == thegame.players[thegame.playerturn]):
                #was the message legit
                if(thegame.getmessage(line, self)):
                    print (time.strftime("%H:%M") + " Legit command was received and processed");

                else:
                    #the message was somehow incorrect, sending special client side code to try again
                    self.__messageLIST__(self, "TRYAGAIN");






    #def dataReceived(self, data):
    #    "As soon as any data is received, write it back."
     #   self.transport.write("Welcome to Chessline. Mikolaj Balcerek, s416040");
     #   print ("Server time: " +  time.strftime("%H:%M"));