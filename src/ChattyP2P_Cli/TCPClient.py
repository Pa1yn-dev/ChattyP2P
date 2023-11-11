import socket
from MessageHandling import *
from Logging import *
from _global import *

def TCPCLIENTMAIN():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((IP, PORT))
        while True:
            print("Enter a message:")
            MSGHANDLER(input(), client)


    
