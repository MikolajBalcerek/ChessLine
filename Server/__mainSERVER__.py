from twisted.internet import reactor, protocol
import SetupTalk;
import time;



class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    connectedplayers = 0;
    playingplayers = 0;

    def connectionMade(self):
        print ("New connection made at: " + time.strftime("%H:%M"));
        Echo.connectedplayers = Echo.connectedplayers + 1;
        self.__helloMessages__();

    def __helloMessages__(self):
        self.transport.write("Welcome to Chessline. Author: Mikolaj Balcerek, s416040 \n");
        self.transport.write("Server time: " + time.strftime("%H:%M") + "\n");
        self.transport.write("Connected players: " + str(Echo.connectedplayers) + "\n");
        self.transport.write("Available players for matchmaking: " + str(Echo.connectedplayers - Echo.playingplayers) + "\n");

    def connectionLost(self, reason):
        Echo.connectedplayers = Echo.connectedplayers - 1;
        print ("Connection Lost");

    #def dataReceived(self, data):
    #    "As soon as any data is received, write it back."
     #   self.transport.write("Welcome to Chessline. Mikolaj Balcerek, s416040");
     #   print ("Server time: " +  time.strftime("%H:%M"));


def main():
    #Ask user for setup data
    SetupTalk.converse_initial_setup();

    #run the server
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(SetupTalk.portnumber, factory)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()