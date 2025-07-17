# --- Import the required libraries / modules:
import machine
from modules.alarm import motion_detected


def main() -> None:
    """_summary_
    This is the main entry point for the program to start.
    """
    
    # --- Define the pins to use:
    motion_sensor = machine.Pin(17, machine.Pin.IN)

    # --- Check the motion sensor for movement and call
    # --- motion_detected when motion is detected:
    while True:
        motion_sensor.irq(trigger = machine.Pin.IRQ_RISING, 
                          handler = motion_detected)


# --- Run the main function:
if __name__ == "__main__":
    main()