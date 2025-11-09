import RPi.GPIO as GPIO  # Import the GPIO library
import time              # Import the time library for delays
# Set the pin numbering mode (BCM refers to the GPIO number, not the pin number)
GPIO.setmode(GPIO.BCM)
# Disable warnings
GPIO.setwarnings(False)
# Set up GPIO pin 17 as an output pin
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)
print("LED Blinking... Press Ctrl+C to exit.")
try:
 # Loop forever
    while True:
        print("LED ON")
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn the LED on
        time.sleep(1)                    # Wait for 1 second
        print("LED OFF")
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn the LED off
        time.sleep(1)                    # Wait for 1 second
except KeyboardInterrupt:
    # This part runs when you press Ctrl+C
    print("Stopping program.")
    GPIO.cleanup()  # Clean up the GPIO pins