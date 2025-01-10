# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("hello world")
    led.value = True
    time.sleep(1.00)
    led.value = False
    time.sleep(1.00)
