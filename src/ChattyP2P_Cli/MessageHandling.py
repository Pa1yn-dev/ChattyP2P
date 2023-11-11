from _global import *

def MSGHANDLER(msg, server):
    msgstring = f"{USERNAME}: {msg}"
    server.send(msgstring.encode())
    print(server.recv(4096).decode('utf-8'))

    return

#def MSGRECV(server):
    #print(server.recv(4096).decode('utf-8'))
    

    
