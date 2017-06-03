from __future__ import print_function
from twisted.internet import reactor, protocol
import SetupTalkClient;
import ClientFactory
import ClientClient;
import time;


# this connects the protocol to a server running on port 8000
def main():
    #Get data from user
    #SetupTalkClient.converse_initial_setup();
    f = ClientFactory.ClientFactory()
    reactor.connectTCP("localhost", SetupTalkClient.portnumber, f)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
