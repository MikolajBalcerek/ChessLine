from twisted.internet import reactor, protocol
import SetupTalk;
import Server;
import time;


def main():
    #Ask user for setup data
    #SetupTalk.converse_initial_setup();

    #run the server
    factory = protocol.ServerFactory()
    factory.protocol = Server.Server
    reactor.listenTCP(SetupTalk.portnumber, factory)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()