# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:04:27 2019

@author: 李鹏飞
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
PWM_Port = GPIO.PWM(12,1000)
PWM_Port.start(50)#DutyCycle
PWM_Port.stop
PWM_Port.ChangeFrequency(1000)
PWM_Port.ChangeDutyCycle(50)