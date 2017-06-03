from twisted.internet import reactor, protocol
import time;

class Server(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    connectedplayers = 0;
    playingplayers = 0;
    matchmakingplayers = 0;

    def connectionMade(self):
        print ("New connection made at: " + time.strftime("%H:%M"));

        Server.connectedplayers = Server.connectedplayers + 1;
        Server.matchmakingplayers = Server.connectedplayers - Server.playingplayers;
        self.__helloMessages__();
        self.__matchMaking__();


    def __helloMessages__(self):
        self.transport.write("Welcome to Chessline. Author: Mikolaj Balcerek, s416040 \n");
        self.transport.write("Server time: " + time.strftime("%H:%M") + "\n");
        self.transport.write("Connected players: " + str(Server.connectedplayers) + "\n");
        self.transport.write("Available players for matchmaking: " + str(Server.matchmakingplayers) + "\n");
        self.transport.write("Please wait to be matched with another player" +  "\n");

    def __matchMaking__(self):
        if (Server.matchmakingplayers >= 2):
            self.transport.write("Found a pair.. Connecting");
            Server.playingplayers = Server.playingplayers + 2;
            Server.matchmakingplayers = Server.matchmakingplayers - 2;

    def connectionLost(self, reason):
        Server.connectedplayers = Server.connectedplayers - 1;
        print ("Connection Lost");


    #def dataReceived(self, data):
    #    "As soon as any data is received, write it back."
     #   self.transport.write("Welcome to Chessline. Mikolaj Balcerek, s416040");
     #   print ("Server time: " +  time.strftime("%H:%M"));