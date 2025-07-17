# --- Import the required libraries / modules:
from machine import ADC


def get_temp_reading() -> dict:
    """_summary_
    
    This is the main function of the program. It will read the value
    of the temperature sensor on a Pico 2 and display it in both
    degree(s) C and F in the terminal.
    
    _returns_
    
    dict: A dictionary with the temperature in both 
          degree(s) C and F.
    """
    
    # --- Define which ADC pin to use to connect to the temp sensor.
    # --- This will always be pin 4 as it is onboard the Pico 1 / 2.
    # --- You can access it using either ADC(4) or ADC(ADC.CORE_TEMP):
    # sensor = ADC(4)
    sensor = ADC(ADC.CORE_TEMP)
    
    # --- Get the digital value of an analogue reading from 
    # --- the temp sensor as a 16-bit value:
    adc_value = sensor.read_u16()
    
    # --- Multiply the adc_value by the max voltage 
    # --- divided by the max value (16-bits) to give the voltage:
    sensor_reading_volts = adc_value * (3.3 / 65535)
    
    # --- Next, convert the reported voltage from the 
    # --- sensor_reading_volts variable and convert it to a celsius value.
    # --- The numbers in the formula is specific to the 
    # --- Pico / Pico 2's temp sensor:
    temperature = 27 - (sensor_reading_volts - 0.706) / 0.001721
    
    # --- Display the temperature to two decimal places.
    # --- Note: using deg. C / F as ° symbol is not supported
    # --- on the Pico 2 due to the lack of extended ASCII
    # --- and the unicode char is not supported for °:

    return {"deg_c": f"{'{:.2f}'.format(temperature)}",
            "deg_f": f"{'{:.2f}'.format(temperature * 9 / 5 + 32)}"}