from _global import *


def MSGHANDLER(msg, client):
    msgstring = f"{USERNAME}: {msg}"
    client.send(msgstring.encode())
    print(server.recv(4096).decode('utf-8'))


    return


    



