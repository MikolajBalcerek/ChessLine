import socket
import sys
import SetupTalk
import Server

SetupTalk.converse_initial_setup();
mainServer = Server.Server.Server(Server.Server(), SetupTalk.address, SetupTalk.portnumber);



