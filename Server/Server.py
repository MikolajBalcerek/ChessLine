from twisted.internet import reactor, protocol
import time;

class Server(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    connectedplayers = 0;
    playingplayers = 0;

    def connectionMade(self):
        print ("New connection made at: " + time.strftime("%H:%M"));
        Server.connectedplayers = Server.connectedplayers + 1;
        self.__helloMessages__();

    def __helloMessages__(self):
        self.transport.write("Welcome to Chessline. Author: Mikolaj Balcerek, s416040 \n");
        self.transport.write("Server time: " + time.strftime("%H:%M") + "\n");
        self.transport.write("Connected players: " + str(Server.connectedplayers) + "\n");
        self.transport.write("Available players for matchmaking: " + str(Server.connectedplayers - Server.playingplayers) + "\n");

    def connectionLost(self, reason):
        Server.connectedplayers = Server.connectedplayers - 1;
        print ("Connection Lost");

    #def dataReceived(self, data):
    #    "As soon as any data is received, write it back."
     #   self.transport.write("Welcome to Chessline. Mikolaj Balcerek, s416040");
     #   print ("Server time: " +  time.strftime("%H:%M"));