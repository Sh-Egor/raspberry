import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
i=20
pin=[24,22,23,27]
while i<25:
  
  for c in pin:
    GPIO.setup(c,GPIO.OUT)
    GPIO.output(c,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(c,GPIO.LOW)
  i+1

