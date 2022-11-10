import socket
from MessageHandling import *
from Logging import *
from _global import *
import threading

def TCPCLIENTMAIN():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((IP, PORT))
            LOGEVENTS_DEBUG("Connecting to server")
        except Exception as ex:
            LOGEVENTS_ERROR(f"{ex}")
            LOGEVENTS_CRITICAL("Terminating CHATTYP2P_Cli")
            quit(code=1)

        
        print("Enter a message in the terminal and press enter to send:")
        while True:
            threading.Thread(target=MSGRECV(client)).start
            MSGHANDLER(input(), client)



    
