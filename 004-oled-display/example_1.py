# --- Import the required libraries / modules:
import machine
from modules.ssd1306 import SSD1306_I2C


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
    
    
    # --- Clear the screen:
    display.fill(0)
    
    # --- Show hello world on the display:
    display.text("-"*127, 0, 0, 1)
    display.text("Hello", 0, 8, 1)
    display.text("World!", 0, 16, 1)
    display.text("-"*127, 0, 24, 1)
    
    display.show()
    
    
if __name__ == "__main__":
    main()