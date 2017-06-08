from __future__ import print_function
from twisted.internet import reactor, protocol
from twisted.protocols import basic
import SetupTalkClient;
import ClientFactory
import GameMode;
import time;

class ClientClient(basic.LineReceiver):

    def __init__(self):
        self.game = 0;


    def connectionMade(self):
        #print "Connected to the server";
        print ("Successful connection");

    def lineReceived(self, line):
        if (str(line) == "GAMEMODE"):
            self.game = GameMode.Gamemode(self);
        elif ((self.game != 0) and (str(line) == "YOUR MOVE")):
            self.game.makeMove();
        elif ((self.game != 0) and (str(line) == "TRYAGAIN")):
            self.game.makeMove();
        elif ((self.game !=0) and (str(line) == "GAMEOVER")):
            self.game = 0;
        elif ((self.game == 0) and (str(line) == "WAITINGMATCH")):
            #when the player has played and decides whether to join the matchmaking
            self.game = 0;
            response = raw_input(time.strftime("%H:%M You:") + " Do you want join the waiting queue and force matchmaking immediately (allow for repeat opponents)? \n");
            if ((str(response) == "MATCH") or (str(response) == "y") or (str(response) == "YES") or (str(response) == "Y") or (str(response) == "Yes") or (str(response) == "yes")):
                self.sendLine("MATCH"); #command code to the server
        else:
            print(time.strftime("%H:%M Server: ") + line);



    #def dataReceived(self, data):
      #  print(time.strftime("%H:%M Server:  ") + data)
      #  self.clearLineBuffer();
        #self.transport.loseConnection():

    def connectionLost(self, reason):
        print("connection lost")
