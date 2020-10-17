# -*- coding: utf-8 -*-

from service import *

from datetime import datetime
import socket
import pickle
import os


__author__ = "Tiago Bratz Heck"
__maintainer__ = "Tiago Bratz Heck"
__version__ = "1.0.1"

    
def client_program():
    """[Main program]

    Connect to the server and send the data using socket module
    """
    host = socket.gethostname()  
    port = 5000 

    client = socket.socket() 
    client.connect((host, port))  

    exp = 7

    print("Current PID: " + str(os.getpid()))

    for _ in range(0, 15):
        start_time = get_time(0)

        size = get_size_data(exp)
        exp += 1

        list_data = get_data(size)

        client.send(pickle.dumps(list_data))  
        data = client.recv(2097152) # 2Exp21

        info, net_info = get_process_analysis(os.getpid())
        end_time = get_time(start_time)  
        print_results(size, end_time) 
        print_process_results(info, net_info)                
   
    client.close() 


# Start client side 
if __name__ == '__main__':
    client_program()