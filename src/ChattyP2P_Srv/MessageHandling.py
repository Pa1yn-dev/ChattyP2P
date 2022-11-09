from _global import *


def MSGHANDLER(msg, client):
    msgstring = f"{USERNAME}: {msg}"
    client.send(msgstring.encode())

    print(client.recv(4096).decode('utf-8'))

    return

def MSGRECV(client):
    print(client.recv(4096).decode('utf-8'))





