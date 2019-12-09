import RPi.GPIO as gpio
import time

led1pin = 24
led2pin = 22
led3pin = 23
led4pin = 27

button1pin = 6
button2pin = 1
button3pin = 7
button4pin = 8

buttonWasPressed = False
ledIsOn = False

def main():
  buttonWasPressed = False
  ledIsOn = False

  gpio.setwarnings(True)
  gpio.cleanup()
  gpio.setmode(gpio.BCM) # Use BCM GPIO numbers

  gpio.setup(led1pin, gpio.OUT, initial = 0)
  gpio.setup(led2pin, gpio.OUT, initial = 0)
  gpio.setup(led3pin, gpio.OUT, initial = 0)
  gpio.setup(led4pin, gpio.OUT, initial = 0)

  gpio.setup(button1pin, gpio.IN)
  gpio.setup(button2pin, gpio.IN)
  gpio.setup(button3pin, gpio.IN)
  gpio.setup(button4pin, gpio.IN)

  while True:
    if gpio.input(button1pin) == False:
      time.sleep(0.02)
      if gpio.input(button1pin) == False:
        buttonWasPressed = True
    else:
      if buttonWasPressed == True:
        print("button was pressed")
        ledIsOn = ~ledIsOn
        gpio.output(led1pin, ledIsOn)
        buttonWasPressed = False
      else:
        print("button was not pressed")

try:
  main()

except KeyboardInterrupt:
  print("Exit pressed Ctrl+C")
except:
  print("Other Exception")
finally:
  gpio.cleanup()
  print("End of program")