from _global import *


def MSGHANDLER(msg, client):
    msgstring = f"{USERNAME}: {msg}"
    client.send(msgstring.encode())

    return

def MSGRECV(server):
    print(server.recv(4096).decode('utf-8'))
    



