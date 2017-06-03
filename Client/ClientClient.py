from __future__ import print_function
from twisted.internet import reactor, protocol
from twisted.protocols import basic
import SetupTalkClient;
import ClientFactory
import GameMode;
import time;

class ClientClient(basic.LineReceiver):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        #print "Connected to the server";
        print ("Successful connection");

    def lineReceived(self, line):
        if (str(line) == "GAMEMODE"):
            GameMode.initialize();
        else:
            print(time.strftime("%H:%M Server: ") + line);



    #def dataReceived(self, data):
      #  print(time.strftime("%H:%M Server:  ") + data)
      #  self.clearLineBuffer();
        #self.transport.loseConnection():

    def connectionLost(self, reason):
        print("connection lost")
