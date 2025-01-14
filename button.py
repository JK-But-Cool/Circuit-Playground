# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
boot = digitalio.DigitalInOut(board.BUTTON_B)
boot.direction = digitalio.Direction.INPUT
boot.pull = digitalio.Pull.DOWN
def thing ():
    print(dir(board))
    print("==============================================================")
    print(dir(digitalio))
    print("==============================================================")
    print(dir(digitalio.DigitalInOut))
    print("==============================================================")
    print(dir(led))
    print("==============================================================")
    while True:
        led.value = boot.value
        time.sleep(1)
        print(boot.value)
thing()