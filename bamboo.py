#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcd8544.lcd as lcd
import unicodedata

from os import environ, geteuid
from PyBambooHR import PyBambooHR
from time import sleep
from sys import exit


def center_and_strip(s):
    return '{:^14}'.format(s)[:14]


def strip_accent(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

if not geteuid() == 0:
    exit('this script must be run as root')

# constants
ON, OFF = [1, 0]

# connect to bambooHR and get the employees' list
bamboo = PyBambooHR(
    subdomain=environ.get('BAMBOOHR_SUBDOMAIN', 'your_subdomain'),
    api_key=environ.get('BAMBOOHR_API_KEY', 'your_api_key')
)
employees = bamboo.get_employee_directory()

try:
    # initialize the LCD screen
    lcd.init()
    lcd.cls()
    lcd.backlight(ON)

    # display the name of each employee
    for employee in employees:
        # clear the screen
        lcd.cls()

        # get the employee first and last name and strip any special character
        # as they're not supported by the LCD lib
        first_name = strip_accent(employee.get('firstName', ''))
        last_name = strip_accent(employee.get('lastName', ''))

        # display, wait a bit and iterate
        lcd.text(center_and_strip(environ.get('BAMBOOHR_SUBDOMAIN', '')))
        lcd.text(center_and_strip(''))
        lcd.text(center_and_strip(first_name))
        lcd.text(center_and_strip(last_name))
        sleep(0.25)
except KeyboardInterrupt:
    pass
finally:
    lcd.cls()
    lcd.backlight(OFF)
