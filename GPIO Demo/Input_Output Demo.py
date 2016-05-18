"""
The following program is used to blink LED when input on pin 12 is HIGH 
If input on pin 12 goes low the LED remains on
The following link can be used to learn more about input/output
https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
"""
#import the GPIO and time modules
import RPi.GPIO as GPIO
import time

#set up pins for input/output
GPIO.setmode(GPIO.BOARD) #select pin numbering according to the board
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) #pull up is used to set the initial value of pin as HIGH
GPIO.setup(16,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(16,GPIO.LOW)

try:
    while True:
        input_state=GPIO.input(12)
        if(input_state==False):		#check if input on pin 12 is LOW
            GPIO.output(16,GPIO.HIGH)
        else:						# the code in this block is used to blink LED
            GPIO.output(16,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(16,GPIO.LOW)
            time.sleep(1)
			
except KeyboardInterrupt:
    GPIO.cleanup()

        
