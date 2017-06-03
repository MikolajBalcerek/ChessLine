import Server;
class Chessgame:

    def __init__(self, serverpassed, twoplayers, idnumber):
        self.playerOne = twoplayers[0];
        self.playerTwo = twoplayers[1];
        self.chessserver = serverpassed;
        self.idonserver = idnumber;

