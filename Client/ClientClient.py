from __future__ import print_function
from twisted.internet import reactor, protocol
from twisted.protocols import basic
import SetupTalkClient;
import ClientFactory
import time;

class ClientClient(basic.LineReceiver):
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
