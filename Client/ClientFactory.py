from __future__ import print_function
from twisted.internet import reactor, protocol
import SetupTalkClient;
import time;
import ClientClient;

class ClientFactory(protocol.ClientFactory):
    protocol = ClientClient.ClientClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - attempt at a simple reconnect mechanism")
        connector.connect()