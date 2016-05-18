"""
The following code is used to blink a LED by changing the duty cycle of a PWM signal
The following link can be used to learn more about PWM
https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/ 
"""
#import the GPIO and time modules
import RPi.GPIO as GPIO
import time 

#set up pins for input/output
GPIO.setmode(GPIO.BOARD) #select pin numbering according to the board 
GPIO.setup(12, GPIO.OUT) 
GPIO.setwarnings(False) # disable warnings is used to disable warnings for pin under use

pwm=GPIO.PWM(12,2) # (pin number,frequency)
pwm.start(0) #(duty cycle)

try:
	while True:
		for i in range(0,100,1):
			pwm.ChangeDutyCycle(i) #changes duty cycle in the range of 0-100 %
			time.sleep(0.1)
		for i in range(100,0,-1):
			pwm.ChangeDutyCycle(i)
			time.sleep(0.1)

except KeyboardInterrupt: #ctrl+c is used for keyboard interrupt
	GPIO.cleanup() #cleans up all ports and resets ports as inputs 
