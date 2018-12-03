import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Set GPIO pin numbering 

TRIG_1 = 21                                  #Associate pin 23 to TRIG
ECHO_1 = 20                                 #Associate pin 24 to ECHO

def sensor_init():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(TRIG_1,GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(ECHO_1,GPIO.IN)   
    
def measure_distance():
    GPIO.output(TRIG_1, False)  
    time.sleep(0.2)
    GPIO.output(TRIG_1, True) 
    time.sleep(0.00001) 
    GPIO.output(TRIG_1, False)
    while GPIO.input(ECHO_1)==0:               #Check whether the ECHO is LOW
        pulse_start_1 = time.time()              #Saves the last known time of LOW pulse
    while GPIO.input(ECHO_1)==1:               #Check whether the ECHO is HIGH
        pulse_end_1 = time.time()                #Saves the last known time of HIGH pulse 
    pulse_duration_1 = pulse_end_1 - pulse_start_1 #Get pulse duration to a variable
    distance_1 = pulse_duration_1 * 17150        #Multiply pulse duration by 17150 to get distance
    distance_1 = round(distance_1, 2)
    #GPIO.output(TRIG_2, False)
    #time.sleep(0.2)
    #GPIO.output(TRIG_2, True) 
    #time.sleep(0.00001) 
    #GPIO.output(TRIG_2, False)
    #while GPIO.input(ECHO_2)==0:               #Check whether the ECHO is LOW
     #   pulse_start_2 = time.time()              #Saves the last known time of LOW pulse
    #while GPIO.input(ECHO_2)==1:               #Check whether the ECHO is HIGH
     #   pulse_end_2 = time.time()                #Saves the last known time of HIGH pulse 
    #pulse_duration_2 = pulse_end_2 - pulse_start_2 #Get pulse duration to a variable
    #distance_2 = pulse_duration_2 * 17150        #Multiply pulse duration by 17150 to get distance
    #distance_2 = round(distance_2, 2)
    #if distance > 2 and distance < 400:      #Check whether the distance is within range
        #print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    #else:
        #print "Out Of Range"                   #display out of range
    return distance_1#, distance_2