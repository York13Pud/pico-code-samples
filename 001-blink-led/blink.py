from machine import Pin
from utime import sleep

# --- Define which GPIO pin to use:
led_gpio = Pin("LED", Pin.OUT)


# --- Blink the LED on and off for 2 seconds
# --- until the loop is broken:
while True:
    try:
        led_gpio.toggle()
        sleep(2)
        
    except KeyboardInterrupt:
        # --- Turn off the LED when the 
        # --- user does ctrl-c to end the program:
        led_gpio.off()
        break
