import socket;

address = 0;
portnumber = 8080;

def converse_initial_setup():
    print "Setting up the client..";
    address = raw_input("Name the ip address you wish to connect to \n");
    while(__verify_adress__(address) == False):
        address = raw_input("Enter a correct ipv4 address: \n");

    portnumber = raw_input("Name the port number the server is listening on: \n");
    while (__verify_adress__(portnumber) == False):
        portnumber = raw_input("Enter a correct port number: \n");

def __verify_adress__(address):
    try:
        socket.inet_aton(address)
        return True;
    except socket.error:
        return False;

def __verify_portnumber__(portnumber):
    try:
        portnumber = portnumber * 1;
        if ((portnumber <= 65535) and (portnumber >= 1)):
            return True;
        else:
            return False;
    except ValueError:
        return False;