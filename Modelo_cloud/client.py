# -*- coding: utf-8 -*-

from service import *
from auth import firebase

from datetime import datetime

import json
import os


__author__ = "Tiago Bratz Heck"
__maintainer__ = "Tiago Bratz Heck"
__version__ = "1.0.1"


def send_data(db: object, path: str, data: dict) -> None:
    """[Send data to cloud]

    Send values to Firebase Cloud Database
    """
    try:
        db.child(path).child("values").set(data)
    except:
        print("Error while setting data")


def retrieve_data(db: object, path: str) -> dict:
    """[Get data from cloud]

    Selecting all the values saved in Firebase Cloud Database
    """
    while True:
        try:
            results = db.child(path).child("values").get() 
            break
            return results
        except:
            print("Error while getting data")


def remove_data(db: object, path: str) -> None:
    """[Remove data]

    Remove the values in Firebase Cloud Database
    """
    try:
        db.child(path).child("values").remove() 
    except:
        print("Error while removing data")

    
def client_program():
    """[Main program]

    Connect to the server and send the data using pyrebase for Firebase Cloud Database
    """
    db = firebase.database()
    exp = 7

    for _ in range(0, 15):

        start_time = get_time(0)

        size = get_size_data(exp)
        exp += 1
        data = get_data(size)

        x = {
            "values": data
        }

        x_to_json = json.dumps(x)

        path = "data"
        send_data(db, path, x_to_json)

        results = retrieve_data(db, path)
               
        info, net_info = get_process_analysis(os.getpid())
        end_time = get_time(start_time)  

        remove_data(db, path)       

        print_results(size, end_time) 
        print_process_results(info, net_info)  


# Start client side 
if __name__ == '__main__':
    client_program()