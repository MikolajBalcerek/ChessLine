import Server;
import chess;
import time;
class Chessgame:

    def __init__(self, serverpassed, twoplayers, idnumber):
        #setting up the game board and Chessgame instance
        self.playerturn = 0;
        self.thisTurnMoveMade = False;
        self.players = twoplayers;
        self.playerOne = twoplayers[0];
        self.playerTwo = twoplayers[1];
        self.chessserver = serverpassed;
        self.idonserver = idnumber;
        self.board = chess.Board();
        self.gameover = False;
        self.playerturn = 0;  # index of player that is ought to make a move
        self.lastplayer = 1; #index of a player that made move last time
        self.__firstTurn__();

    def __newBoardState__(self):
        #This sends out the board state to both players
        self.chessserver.__messageLIST__(self.players, str("\n" + str(self.board)));
        print (time.strftime("%H:%M") + " GAME STATUS. ID = " + str(self.idonserver));
        print (self.board);



    def __firstTurn__(self):
        self.playerturn = 0;  # index of player that is ought to make a move
        self.lastplayer = 1;  # index of a player that made move last time
        self.__newBoardState__();
        messagereceivers = [];
        messagereceivers.append(self.players[self.playerturn]);
        self.chessserver.__messageLIST__(messagereceivers, "YOUR MOVE");
        print (time.strftime("%H:%M") + " Waiting for a move from player, game ID = " + str(self.idonserver));


    def __AfterMove__(self):
        #Verify if both players are still connected
        if (self.__isplayerconnected__(self.playerOne) and self.__isplayerconnected__(self.playerTwo)):
            #draw conditions
            if not (self.board.is_stalemate()):
                if not (self.board.is_insufficient_material()):
                    #has the game been won
                    if not (self.board.is_checkmate()):
                        if not (self.gameover):
                            #WE GET TO PLAY, HURRAY
                            # sending board state to players
                            self.__newBoardState__();

                            # changing turns
                            self.thisTurnMoveMade = False;
                            self.playerturn = (self.playerturn + 1) % 2;
                            self.lastplayer = (self.lastplayer + 1) % 2;

                            #message next player of his turn
                            messagereceivers = [];
                            messagereceivers.append(self.players[self.playerturn]);
                            self.chessserver.__messageLIST__(messagereceivers,"YOUR MOVE");

                    else:
                        #player who made the last move won
                        list = [];
                        list.append(self.players[self.playerturn]);
                        listtwo = [];
                        listtwo.append(self.players[self.lastplayer]);
                        self.__declareloser__(listtwo, "Checkmate");
                        self.__declarewinner__(list, "Checkmate");
                else:
                    #is a stalemate due to insufficient material
                    self.__draw__("Insufficient material");

            else:
                 #is a stalemate
                self.__draw__("Stalemate");


        else:
            #one of the players has disconnected
            #declaring winners
            if not (self.__isplayerconnected__(self.playerOne)):
                self.__declarewinner__(self.playerTwo, "Your opponent has disconnected");
            else:
                self.__declarewinner__(self.playerOne, "Your opponent has disconnected");




    def __isplayerconnected__(self, player):
        if (player in self.chessserver.clients_list):
            return True;
        else:
            self.players.pop(player);
            return False;


    def __declarewinner__(self, player, reason):
        self.chessserver.__messageLIST__(player, "YOU WON!");
        self.chessserver.__messageLIST__(player, reason);
        self.__gameover__();

    def __declareloser__(self, player, reason):
        self.chessserver.__messageLIST__(player, "YOU LOST!");
        self.chessserver.__messageLIST__(player, reason);

    def __draw__(self, reason):
        self.chessserver.__messageLIST__(self.players, "The game has ended in a draw.")
        self.chessserver.__messageLIST__(self.players, reason);
        self.__gameover__();

    def playerDisconnected(self, player):
        if (self.playerOne == player):
            list = [];
            list.append(self.playerTwo);
            self.__declarewinner__(list, "Your opponent has disconnected");
        elif (self.playerTwo == player):
            list = [];
            list.append(self.playerOne);
            self.__declarewinner__(list, "Your opponent has disconnected");



    def __gameover__(self):
        print ("The game has ended. ID = " + str(self.idonserver));
        self.chessserver.__messageLIST__(self.players, "GAMEOVER");
        self.gameover = True;
        #remove the players from playing list
        #add the players to waiting list
        #remove the game from the gameslist


    def getmessage(self, message, player):
        #processes messages and return True/False depending if it was valid
        if (str(message) == "FORFEIT"):
            if(player == self.players[0]):
                list = [];
                list.append(self.players[1]);
                self.__declarewinner__(list, "The opposite player has forfeited the game");
                return True;
            else:
                list = [];
                list.append(self.players[0]);
                self.__declarewinner__(list, "The opposite player has forfeited the game");
                return True;

        elif (self.__verifymove__(message) == True):
            self.__makemove__(message);
            return True;
        else:
            list = [];
            list.append(player);
            self.chessserver.__messageLIST__(list, "Incorrect command, try again")
            return False;


    def __verifymove__(self, message):
        #verifies moves
        try:
            if (chess.Move.from_uci(message) in self.board.legal_moves):
                return True;
            else:

                return False;
        except (ValueError, IndexError) as wrongformatorillegalmove:
            return False;


    def __makemove__(self, message):
        #Makes the move on the board
        self.board.push_uci(message);
        self.thisTurnMoveMade = True;





