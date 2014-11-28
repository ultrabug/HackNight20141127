HackNight20141127
=================

Raspberry Pi, Nokia screen and BambooHR


1 - *Get* your Raspi
------------------

- Raspbian
- SSH already enabled

2 - *Get* your WiFi
-----------------

- Plug keyboard/monitor
- Configure WiFi

3 - *Get* your screen
-------------------

- The hardware:
	- [Nokia 5110 screen](http://www.dx.com/p/replacement-1-6-lcd-screen-with-blue-backlight-for-nokia-5110-blue-145860#.VHhCZFTN-Cg)
	- 8 wires
- Instructions from https://github.com/XavierBerger/pcd8544
	- install wiringpi2 + python bindings
	- install python lib for screen
	- wire **carefully** the LCD to the Raspi, using `gpio readall` as a reference
- run some examples

4 - *Get down* with the BambooHR API
------------------------------------

- `pip install PyBambooHR`
- API doc: http://www.bamboohr.com/api/documentation
	- get employees list: http://www.bamboohr.com/api/documentation/employees.php#getEmployeeDirectory
	- get time off list: http://www.bamboohr.com/api/documentation/time_off.php


Get, get, get, get down! [Whoooo!](http://www.youtube.com/watch?v=h6kvY5g9KJY)
