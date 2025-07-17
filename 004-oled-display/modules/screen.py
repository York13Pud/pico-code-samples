import machine
from .ssd1306 import SSD1306_I2C
# --- https://github.com/PerfecXX/MicroPython-SSD1306/tree/main


def init_screen(i2c_bus: int = 0, sda_pin: int = 0, scl_pin: int = 1, bus_freq: int = 400000, x_size: int = 128, y_size: int = 32) -> object:
    """_summary_

    Args:
        i2c_bus (int, optional): The i2c bus number to use. Defaults to 0.
        sda_pin (int, optional): The pin on the Pico 2 to use for sda. Defaults to 0.
        scl_pin (int, optional): The pin on the Pico 2 to use for scl. Defaults to 1.
        bus_freq (int, optional): The bus frequency to use. Defaults to 400000.
        x_size (int, optional): The pixel width of the display. Defaults to 128.
        y_size (int, optional): The pixel height of the display. Defaults to 32.

    Returns:
        object: An object for interacting with the display.
    """
    
    # --- Setup the driver for the display:
    sda = machine.Pin(sda_pin) # GP0
    scl = machine.Pin(scl_pin) # GP1
           
    i2c = machine.I2C(i2c_bus, sda = sda, scl = scl, freq = bus_freq)
    
    display_x = x_size
    display_y = y_size
    
    display = SSD1306_I2C(display_x, 
                          display_y, 
                          i2c)
    
    return display