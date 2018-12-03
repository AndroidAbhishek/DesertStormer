#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import hcsr04
import kalmanfilter
import os
import pygame

car_length = 16

INDICATOR_GREEN = 16
INDICATOR_RED = 12 

def main():
  GPIO.setmode(GPIO.BCM) 
  GPIO.setup(INDICATOR_GREEN,GPIO.OUT)
  GPIO.setup(INDICATOR_RED,GPIO.OUT)
  hcsr04.sensor_init()
  time.sleep(3)
  measurements = []
  counter = 2
  initial_position = 0
  pygame.mixer.init()
  while True:
    i=0
    for i in range(counter):
        distance_from_goal = hcsr04.measure_distance()
        measurements.append(distance_from_goal)
        if abs(distance_from_goal- initial_position) > 0.5:
            print "Rover in motion"
            #os.system('mpg123 -q notification_move.mp3 &')
            GPIO.output(INDICATOR_GREEN,True)
            initial_position = distance_from_goal
        else:
            GPIO.output(INDICATOR_GREEN,False)
            print "Rover Still"
        time.sleep(0.2)
    #localized_x = kalmanfilter.kalman_filter(measurements)
    #measurements = []
    #print "Estimated Position: ",localized_x[0]

    
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print "Interrupt"
    time.sleep(1)
