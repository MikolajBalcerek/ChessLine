from __future__ import print_function
from twisted.internet import reactor, protocol
import SetupTalkClient;
import time;

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        #print "Connected to the server";
        print ("Successful connection");

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print(time.strftime("%H:%M Server:  ") + data)
        #self.transport.loseConnection()

    def connectionLost(self, reason):
        print("connection lost")


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    #Get data from user
    SetupTalkClient.converse_initial_setup();
    f = EchoFactory()
    reactor.connectTCP("localhost", SetupTalkClient.portnumber, f)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
