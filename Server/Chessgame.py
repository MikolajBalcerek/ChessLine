import Server;
import chess;
import time;
class Chessgame:

    def __init__(self, serverpassed, twoplayers, idnumber):
        #setting up the game board and Chessgame instance
        self.players = twoplayers;
        self.playerOne = twoplayers[0];
        self.playerTwo = twoplayers[1];
        self.chessserver = serverpassed;
        self.idonserver = idnumber;
        self.board = chess.Board();
        self.__gameloop__();

    def __newBoardState__(self):
        #This sends out the board state to both players
        self.chessserver.__messageLIST__(self.players, str("\n" + str(self.board)));
        print (time.strftime("%H:%M") + " GAME STATUS. ID = " + str(self.idonserver));
        print (self.board);


    def __gameloop__(self):
        #this is the main gameloop
        playerturn=0; #index of player that is ought to make a move

        while (True):
            #When both players are connected
            if (self.__isplayerconnected__(self.playerOne) and self.__isplayerconnected__(self.playerTwo)):
                #sending board state to players
                self.__newBoardState__();
                #win conditions
                #if not (self.board.is_game_over()):
                break;

            else:
                #one of the players has disconnected
                #declaring winners
                if not (self.__isplayerconnected__(self.playerOne)):
                    self.__declarewinner__(self.playerTwo, "Your opponent has disconnected");
                else:
                    self.__declarewinner__(self.playerOne, "Your opponent has disconnected");

                #breaking out of the game loop
                break;






            playerturn = (playerturn + 1)%2;



    def __isplayerconnected__(self, player):
        if (player in self.chessserver.clients_list):
            return True;
        else:
            return False;


    def __declarewinner__(self, player, reason):
        self.chessserver.__messageLIST__(player, "YOU WON!");
        self.chessserver.__messageLIST__(player, reason);

    #def __gameover__(self):


       # if(chess.isgameover)
            #you won
            #you lost
            #remove the game and players and return them to lobbby as matchmaking players





