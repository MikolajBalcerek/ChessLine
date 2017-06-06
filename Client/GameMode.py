import ClientClient;
import ClientFactory;
import time;

class Gamemode:

    def __init__(self, client):
        self.client = client;
        print ("-------------------------------------------------------");
        print (time.strftime("%H:%M ") + "You: Type FORFEIT to surrender");
        print (time.strftime("%H:%M ") + "You: Type moves in UCI, long algebraic notation, e.g e2e4");

    def makeMove(self):
        print (time.strftime("%H:%M ") + "You: It's time for you to make a move or issue a command!");
        command = raw_input("Your command: ");
        self.client.sendLine(str(command));
        print (time.strftime("%H:%M ") + "You: Sent!");

        if(str(command) == "FORFEIT"):
            print (time.strftime("%H:%M ") + "You: You have forfeited the game");


