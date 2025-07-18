# Raspberry Pi Pico Sample Code

In this repository, there is a collection of code examples for use with the Pico and Pico 2 boards.

## Instructions

The instructions for each program are contained in the README.md file in the/each program(s) folder.

## Link to Programs

* [Blink the onboard LED](/001-blink-led/) - This is a simple program that will blink the onboard LED of a Pico or Pico on and off every two seconds.
* [Read the onboard temperature sensor](/002-temperature-sensor/) - This is a program that will get a reading from the onboard temperature sensor and print it out in both celsius and fahrenheit.
* [Scan for and setup a Wi-Fi connection](/003-wifi-network/) - There are two programs in this folder:
  * wifi_scan.py: This allows the Pico 2 W to scan for nearby Wi-Fi networks and list each one.
  * wifi_connection.py: This sets up the Pico 2 W to connect to a Wi-Fi network and send a HTTPS request to Google and print out the status code from the request, along with two parts of the header.
* [Displaying text and images on an OLED display](/004-oled-display/) - This has three examples of how you can display text and images on an OLED display that is attached to a Pico 2.
* [Building a simple burglar alarm with a PIR motion sensor](/005-pir-alarm/) - This is a simple project that covers how you can use a Pico 2, along with a PIR motion sensor, a buzzer and an LED (onboard the Pico 2) to build a burglar / intruder alarm.