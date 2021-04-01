#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 05:01:38 2021

@author: DariusSzablowski
"""

import csv
  
# sending the uptime command as an arguement to popen() 
# and saving the returned result (after truncating the trailing \n) 

with open('/Users/DariusSzablowski/Desktop/uptime tracker/data/log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["start", "shutdown"])



# HOW TO RUN A PYTHON SCRIPT AT STARTUP
# https://stackoverflow.com/questions/29338066/run-python-script-at-os-x-startup

# HOW TO RUN A PYTHON SCRIPT BEFORE SHUTDOWN
# https://gist.github.com/RxDx/0e6587e2adc2d2ac02e91e4e654227af
# bzw.: https://apple.stackexchange.com/questions/107366/run-script-before-restart-shutdown

# https://stackoverflow.com/questions/6442364/running-script-upon-login-mac
# https://superuser.com/questions/1164706/how-do-i-make-a-python-file-executable-on-macos-sierra
