# --- Import the required libraries:
import binascii
import network
import rp2


def main() -> None:
    """_summary_
    
    This is where the program code is stored. This will scan for
    Wi-Fi networks and print a list of any discovered Wi-Fi networks.
    
    _returns_
    
    None: Nothing is returned
    """
    
    # --- Setup the network configuration:
    rp2.country("GB")

    # --- Create a Wi-Fi interface and activate it:
    wlan = network.WLAN(network.STA_IF) # STA_IF = Use as Wi-Fi client
    wlan.active(True) # Activate the Wi-Fi interface

    # --- Scan for Wi-Fi networks.
    # --- Creates a list of tuples, each with 6 fields:
    # --- ssid, bssid, channel, RSSI, security, hidden:
    discovered_networks = wlan.scan()

    # --- Show the list of discovered Wi-Fi networks:
    print(discovered_networks)

    # --- Create an empty list:
    wifi_networks = list()

    for i in discovered_networks:
        # --- Append a dictionary to wifi_networks with each
        # --- entry having a descriptive key:
        wifi_networks.append(
            {
            "ssid": i[0].decode(), 
            "ap-mac-address": binascii.hexlify(i[1]).decode(),
            "channel-number": i[2],
            "rssi-strength": i[3],
            "security": i[4],
            "hidden": i[5]
            }
        )

        # --- Another option is to just print out the current Wi-Fi networks details:
        print(i[0].decode(), binascii.hexlify(i[1]).decode(), i[2], i[3], i[4], i[5])
    
    # --- Show the dictionaries in wifi_networks:
    print(wifi_networks)


# --- Link for RSSI meaning:
# https://www.metageek.com/training/resources/understanding-rssi/

# --- Run the main function:
if __name__ == "__main__":
      main()