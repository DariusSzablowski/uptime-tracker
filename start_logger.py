#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:12:00 2021

@author: DariusSzablowski
"""

import csv
import time
from datetime import date

today = date.today()

# dd/mm/YY
date = today.strftime("%d/%m/%Y")

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
date_plus_time = date + "-" + current_time

filename = '/Users/DariusSzablowski/Desktop/uptime tracker/data/log.csv'

with open(filename, 'rb') as fh:
    first = next(fh).decode()

    fh.seek(-1024, 2)
    last = fh.readlines()[-1].decode()
    last_char = last[-1]
    
    if ord(last_char) == ord('\n'):
        with open(filename, 'a+') as file:
            file.write(date_plus_time)
    # else: do nothing ;)



# print(date_plus_time)

# https://stackoverflow.com/questions/9282967/how-to-open-a-file-using-the-open-with-statement
