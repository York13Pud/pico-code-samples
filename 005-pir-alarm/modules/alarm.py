# --- Import the required libraries / modules:
import machine
from time import sleep_ms


# --- Define the pins to use:
led = machine.Pin("LED", machine.Pin.OUT)
buzzer = machine.Pin(27, machine.Pin.OUT)


def motion_detected(pin) -> None:
    """_summary_
    This function will print the warning to the console, sound the buzzer and blink the LED if pin has any value.    
    
    Args:
        pin (int): Signifies if an interrupt has been triggered (1). 
    """
    
    sleep_ms(100)
    
    # --- Run if pin has a value (typically 1 to run):
    if pin.value():
        print("Danger Will Robinson! Danger!")
    
        for _ in range(20):
            led.toggle()
            buzzer.toggle()
            sleep_ms(100)