import RPi.GPIO as GPIO                 
import time                             
import sys, traceback                  

try:
    
    GPIO.setmode(GPIO.BCM)                 

    pinsLED=[24, 23, 27]                 
    pinsBtnsPullUp=[6, 8]              
    pinsBtnsPullDown=[7]                
    GPIO.setup(pinsLED, GPIO.OUT)                           

    GPIO.setup(pinsBtnsPullUp, GPIO.IN)       
    GPIO.setup(pinsBtnsPullDown, GPIO.IN)   

    dictLED={24:6, 
             23:7, 
             27:8} 
             
     
    while 1:
        for i in pinsLED:
            
            if GPIO.input(i) == GPIO.input(dictLED[i]):
              if GPIO.input(i) == GPIO.HIGH:
                GPIO.output(i, GPIO.LOW)
              else:
                GPIO.output(i, GPIO.HIGH)   
except KeyboardInterrupt:
    
    print("Exit pressed Ctrl+C")        
except:
    
    print("Other Exception")                
    print("--- Start Exception Data:")
    traceback.print_exc(limit=2, file=sys.stdout) 
    print("--- End Exception Data:")
finally:
    print("CleanUp")                    
    GPIO.cleanup()                      
    print("End of program")                                 