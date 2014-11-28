#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcd8544.lcd as lcd
import unicodedata
import urllib

from os import environ, geteuid
from PIL import Image
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

    # display the photo of each employee with his first name
    # next to it
    for employee in employees:
        # get the jpg photo and convert it to a usable bitmap
        img = urllib.urlretrieve(employee.get('photoUrl'))[0]
        bmp = Image.open(img)
        bmp = bmp.resize((48, 84), Image.NEAREST).convert('1')
        bmp.save('/tmp/employee.bmp')

        # clear and load the bitmap photo
        lcd.cls()
        lcd.load_bitmap('/tmp/employee.bmp')

        # get the employee display name, strip any special character
        # from his name and get his first name
        display_name = employee.get('displayName', '')
        display_name = strip_accent(display_name)
        first_name = display_name.split(' ')[0]

        # display the first name, wait a bit and iterate
        lcd.text(center_and_strip(first_name))
        sleep(0.25)
except KeyboardInterrupt:
    pass
finally:
    lcd.cls()
    lcd.backlight(OFF)
