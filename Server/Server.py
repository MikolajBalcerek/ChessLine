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
        print ("New connection made at: " + time.strftime("%H:%M"));
        Server.clients_list.append(self);
        Server.connectedplayers = Server.connectedplayers + 1;
        Server.matchmakingplayers = Server.connectedplayers - Server.playingplayers;
        self.__helloMessages__()
        self.__messageLIST__(Server.waiting_list, "New player has connected and wants to play! \n");
        Server.waiting_list.append(self);
        self.__matchMaking__();


    def __messageLIST__(self, listofusers, text):
        for c in listofusers:
            c.transport.write(text);


    def __helloMessages__(self):
        self.transport.write("Welcome to Chessline. Author: Mikolaj Balcerek, s416040 \n");
        self.transport.write("Server time: " + time.strftime("%H:%M") + "\n");
        self.transport.write("Connected players: " + str(Server.connectedplayers) + "\n");
        self.transport.write("Available players for matchmaking: " + str(Server.matchmakingplayers) + "\n");

    def __matchMaking__(self):
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
            self.__messageLIST__(__twoplayers__, "\n\nFound a pair.. Connecting \n");
        else:
            #Not enough players, you have to wait!
            self.transport.write("Please wait to be matched with another player" + "\n");


    def connectionLost(self, reason):
        Server.connectedplayers = Server.connectedplayers - 1;
        Server.clients_list.remove(self);
        if (self in Server.waiting_list):
            Server.waiting_list.remove(self);
        print ("Connection Lost");


    #def dataReceived(self, data):
    #    "As soon as any data is received, write it back."
     #   self.transport.write("Welcome to Chessline. Mikolaj Balcerek, s416040");
     #   print ("Server time: " +  time.strftime("%H:%M"));