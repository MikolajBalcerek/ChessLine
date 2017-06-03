from twisted.internet import reactor, protocol
from twisted.protocols import basic
import time;
import __mainSERVER__;

class Server(basic.LineReceiver):
    """This is just about the simplest possible protocol"""

    connectedplayers = 0;
    playingplayers = 0;
    matchmakingplayers = 0;
    clients_list = [];
    waiting_list = [];

    def connectionMade(self):
        #what happens when somebody connects
        print ("New connection made at: " + time.strftime("%H:%M"));
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

            #Preparing a shortlist of matchmade players
            __twoplayers__ = [];
            __twoplayers__.append(Server.waiting_list.pop(0));
            __twoplayers__.append(Server.waiting_list.pop(0));

            #Maintaining lists and numbers
            Server.playingplayers = Server.playingplayers + 2;
            Server.matchmakingplayers = Server.matchmakingplayers - 2;

            #Messaging players that a game has been found
            self.__messageLIST__(__twoplayers__, "Found a pair.. Connecting");
            print ("Matchmaking two players..");

            #Sending over the command codes to initialize game modes on clients
            self.clearLineBuffer();
            __twoplayers__[0].sendLine("GAMEMODE");
            __twoplayers__[1].sendLine("GAMEMODE");
        else:
            #Not enough players, you have to wait!
            self.sendLine("Please wait to be matched with another player");


    def connectionLost(self, reason):
        #Handling dropped connections
        Server.connectedplayers = Server.connectedplayers - 1;
        Server.clients_list.remove(self);
        if (self in Server.waiting_list):
            Server.waiting_list.remove(self);
            Server.matchmakingplayers = Server.matchmakingplayers - 1;
        print ("Connection Lost");


    #def dataReceived(self, data):
    #    "As soon as any data is received, write it back."
     #   self.transport.write("Welcome to Chessline. Mikolaj Balcerek, s416040");
     #   print ("Server time: " +  time.strftime("%H:%M"));