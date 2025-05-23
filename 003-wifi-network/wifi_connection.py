# --- Import the required libraries:
import network
import rp2
import time
import urequests


def main() -> None:
    """_summary_
    
    This is where the program code is stored. This will attempt to connect to a
    Wi-Fi network. If it can, it will attempt to connect to a URL and return the
    status code.
    
    _returns_
    
    None: Nothing is returned
    """
    
    # --- Setup the network configuration:
    rp2.country("GB")
    ssid = "change-me"
    psk = "change-me"

    # --- Create a new Wi-Fi client and connection to the Wi-Fi network:
    wlan = network.WLAN(network.STA_IF)
    wlan.config(pm = 0xa11140) # --- Sets low power mode to off.
    wlan.active(True)
    
    print(f"Connecting to Wi-Fi network {ssid}")
    wlan.connect(ssid, psk)

    max_wait = 10
    
    # --- Check the connection status:
    while max_wait > 0:
        print(f"Status: {wlan.status()}")
        
        if wlan.status() < 0 or wlan.status() >= 3:
            print(f"Break Status: {wlan.status()}")
            break
        
        max_wait -= 1
        
        time.sleep(1)
        
    # --- 
    if wlan.status() != 3:
        # --- Disconnect from the network and deactivate the Wi-Fi interface:
        wlan.disconnect()
        wlan.active(False)
        
        # --- Raise an error and terminate the program:
        raise RuntimeError(f"Connection to Wi-Fi network {ssid} failed.")
    
    else:
        # --- Display the details of the Wi-Fi's interface config:
        print(f"Connected to Wi-Fi network {ssid}\n")
        
        print(f"IP Address:  {wlan.ifconfig()[0]}")
        print(f"Subnet Mask: {wlan.ifconfig()[1]}")
        print(f"Gateway IP:  {wlan.ifconfig()[2]}")
        print(f"DNS Server:  {wlan.ifconfig()[3]}")
        
        # --- Perform a check on a website to see if the Pico can connect to it:            
        response = urequests.get("https://www.google.com")
        
        print(response.status_code)
        print(response.headers["Date"])
        print(response.headers["Content-Type"])
        
        response.close()
        
        # --- Disconnect from the network and deactivate the Wi-Fi interface:
        wlan.disconnect()
        wlan.active(False)
        

# --- Run the main function:
if __name__ == "__main__":
      main()