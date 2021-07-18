import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
pump_pin = machine.Pin(16, machine.Pin.OUT)
time_since_toggle = 0

while True:
    led_onboard.toggle()
    utime.localtime()
    utime.sleep(1)
    time_since_toggle += 1
    
    if time_since_toggle >= 43200:
        time_since_toggle = 0
        pump_pin.toggle()
        utime.sleep(10)
        pump_pin.toggle()