import machine
import time

led = machine.Pin(15, machine.Pin.OUT)
while True:
    led.value(1)
    time.sleep(0.05)
    led.value(0)
    time.sleep(0.17)
    led.value(1)
    time.sleep(0.05)
    led.value(0)
    time.sleep(1.55)
