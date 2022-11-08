import socket
from Logging import *
from _global import *
from MessageHandling import *
import os

def TCPSRVMAIN():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
        try:
            server.bind((IPADDRESS, PORT))
            LOGEVENTS_DEBUG("Bound to socket")
        except Exception as ex:
            LOGEVENTS_ERROR(f"{ex}")
            LOGEVENTS_CRITICAL("Terminating CHATTY_SRV_PY")
            quit(code=1)

        server.listen(1)
        LOGEVENTS_DEBUG(f"Server listening on {PORT}")

        LOGEVENTS_INFO("Waiting for client connection")

        client, address = server.accept()
        LOGEVENTS_DEBUG(f"Client connected to {address}")

        while True:
            print("Enter a message:")
            MSGHANDLER(input(), client)

        


