# --- Import the required libraries / modules:
from framebuf import FrameBuffer, MONO_HLSB

from modules.pacman import pacman_image
from modules.screen import init_screen


def main() -> None:
    
    # --- Instantiate the screen:
    display = init_screen()
    
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