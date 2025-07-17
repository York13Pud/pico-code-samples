# --- Import the required libraries / modules:
from utime import sleep

from modules.screen import init_screen
from modules.temp_sensor import get_temp_reading

def main() -> None:

    # --- Instantiate the screen:
    display = init_screen()

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