# --- Import the required libraries / modules:
import machine
from modules.ssd1306 import SSD1306_I2C

from utime import sleep

from modules.temp_sensor import get_temp_reading

def main() -> None:
    
    # --- Setup the driver for the display:
    sda = machine.Pin(0) # GP0
    scl = machine.Pin(1) # GP1
           
    i2c = machine.I2C(0, sda = sda, scl = scl, freq=400000)
    
    display_x = 128
    display_y = 32
    
    display = SSD1306_I2C(display_x, 
                          display_y, 
                          i2c) # Cannot pass address. Default is 0x3C.
    
    # --- Update the screen with the temperature
    # --- every 10 seconds:
    while True:
        # --- Get the current temperature:
        temperatures = get_temp_reading()
        
        # --- Clear the screen:
        display.fill(0)
        
        # --- Show the temperature readings on the screen:
        display.text("Current Temps", 0, 0, 1)
        display.text("-"*127, 0, 8, 1)
        display.text(f"Temp C: {temperatures["deg_c"]}", 0, 16, 1)
        display.text(f"Temp F: {temperatures["deg_f"]}", 0, 24, 1)
        
        display.show()
        sleep(10)
    
if __name__ == "__main__":
    main()