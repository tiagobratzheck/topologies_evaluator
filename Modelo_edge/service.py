# -*- coding: utf-8 -*-

from datetime import datetime
import random
import os
import psutil

__author__ = "Tiago Bratz Heck"
__maintainer__ = "Tiago Bratz Heck"
__version__ = "1.0.1"


def get_size_data(exp: int) -> int:      
    """[Return an integer number]

    Result of exponential calculation of 2 and the integer given
    """    
    return 2 ** exp


def get_data(size: int) -> list:
    """[Return a list]

    List of integer numbers determined by the size given
    """
    data = [ random.randint(1, size) for i in range(0, size) ]
    return data


def get_time(time: float) -> float:
    """[Return a float]

    Depending on the variable given, start time or calculate a period of time
    """
    if time == 0:
        start = datetime.now()
        return start
    else:
        return ( datetime.now() - time )


def get_process_analysis(pid: int) -> dict:
    """[Return a dict]

    Dictionary results of psutil class Process with data about the curent process 
    """
    p = psutil.Process(pid)    
    info = p.as_dict()
    net_info = psutil.net_io_counters()
    return info, net_info


def print_results(data: int, time: float) -> str:    
    """[Print data results]

    Result of data size and time processing
    """
    print('\nData size: '                 + str(data) 
         + '\nReceived from server in: '  + str(round((time.seconds / 60), 2)) 
         + ' minutes and '                + str(time.seconds) 
         + ' seconds and '                + str(time.microseconds) 
         + ' microseconds.'
         )   


def print_process_results(info: dict, net_info: dict) -> str:
    """[Print process data results]

    Result of process data
    """
    print("PID: "             + str(info.get('pid'))  
         + "\nCPU PERCENT: "  + str(info.get('cpu_percent'))
         + "\nCPU TIMES: "    + str(info.get('cpu_times'))
         + "\nNUM THREADS: "  + str(info.get('num_threads')) 
         + "\nMEMORY %: "     + str(info.get('memory_percent'))
         + "\nMEMORY INFO: "  + str(info.get('memory_info'))        
         + "\nNETWORk INFO: " + str(info.get('io_counters'))  
        )
    print("\nNetwork informations: " + str(net_info))    