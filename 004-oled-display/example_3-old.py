# --- Import the required libraries / modules:
import machine

from framebuf import FrameBuffer, MONO_HLSB

from modules.pacman import pacman_image
from modules.ssd1306 import SSD1306_I2C
# --- https://github.com/PerfecXX/MicroPython-SSD1306/tree/main

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
    
    # --- Load the pacman image into a framebuffer:
    image_fb = FrameBuffer(pacman_image, 32, 32, MONO_HLSB)

    # --- Show the image on the display and show
    # --- some pacman dots after it:
    display.fill(0)
    
    # --- Load the framebuffer into the display:
    display.blit(image_fb, 0, 0)
    
    # --- Setup three dots to be drawn on the display:
    display.circle(50, 16, 5, 1, 1)
    display.circle(75, 16, 5, 1, 1)
    display.circle(100, 16, 5, 1, 1)    
    
    # --- Show the images and dots on the display:
    display.show()

    
if __name__ == "__main__":
    main()