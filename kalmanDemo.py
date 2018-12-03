import time
import hcsr04
import kalmanfilter

car_length = 16

def main():
  hcsr04.sensor_init()
  time.sleep(1)
  counter = 2
  while True:
    i=0
    for i in range(counter):
        distance_from_goal = hcsr04.measure_distance()
        print distance_from_goal
    
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print "Interrupt"
    time.sleep(1)
