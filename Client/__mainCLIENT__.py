from __future__ import print_function
from twisted.internet import reactor, protocol
import SetupTalkClient;
import ClientFactory
import ClientClient;
import time;


def main():
    #Get data from user
    SetupTalkClient.converse_initial_setup();
    f = ClientFactory.ClientFactory()
    reactor.connectTCP(str(SetupTalkClient.address), SetupTalkClient.portnumber, f)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
