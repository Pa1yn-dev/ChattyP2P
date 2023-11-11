from _global import *

def MSGHANDLER(msg, server):
    msgstring = f"{USERNAME}: {msg}"
    server.send(msgstring.encode())

    return

def MSGRECV(server, task):
    print(server.recv(4096).decode('utf-8'))
    task.join()
    


