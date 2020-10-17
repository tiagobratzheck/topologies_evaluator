# -*- coding: utf-8 -*-

from service import *

import socket
import pickle
import os


__author__ = "Tiago Bratz Heck"
__maintainer__ = "Tiago Bratz Heck"
__version__ = "1.0.1"


def server_program():
    """[Main program]

    Receive data from the client and send them back
    """

    host = socket.gethostname()
    port = 5000 

    server = socket.socket()      
    server.bind((host, port))  
    server.listen()

    conn, address = server.accept()  
    print("\nConnection from: " + str(address))

    while True:    
        data = conn.recv(2097152) # 2Exp21
        if not data:            
            break  
        conn.send(pickle.dumps(data))

    conn.close() 


# Start server side
if __name__ == '__main__':
    server_program()