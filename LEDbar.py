import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledPins = [37, 38, 40, 12, 16, 18, 13, 36, 32, 15]

adc = ADCDevice()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPins, GPIO.OUT)   
    GPIO.output(ledPins, GPIO.HIGH)
    global adc
    if(adc.detectI2C(0x4b)): 
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)

def loop():
    while True:
        value = adc.analogRead(0)
        if value in range(0,27):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[0],GPIO.LOW)
        if value in range(26,53):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[1],GPIO.LOW)
        if value in range(52,79):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[2],GPIO.LOW)
        if value in range(78,105):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[3],GPIO.LOW) 
        if value in range(104,131):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[4],GPIO.LOW)
        if value in range(130,157):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[5],GPIO.LOW)
        if value in range(156,183):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[6],GPIO.LOW) 
        if value in range(182,209):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[7],GPIO.LOW)
        if value in range(208,235):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[8],GPIO.LOW)
        if value in range(234,257):
            GPIO.output(ledPins,GPIO.HIGH)
            GPIO.output(ledPins[9],GPIO.LOW)
        
        
        
        
        print(value)
        time.sleep(0.1)
    
        
def destroy():
    GPIO.cleanup()                     # Release all GPIO

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()   