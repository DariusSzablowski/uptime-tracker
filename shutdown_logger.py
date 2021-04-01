#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:57:02 2021

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

with open('/Users/DariusSzablowski/Desktop/uptime tracker/data/log.csv', 'a+') as file:
    file.write("," + date_plus_time + '\n')


