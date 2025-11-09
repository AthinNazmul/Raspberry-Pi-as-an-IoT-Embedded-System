import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set up the LED pin as an output
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)
# Set up the Button pin as an input
BUTTON_PIN = 27
# We use a pull-down resistor to ensure the input is 0 (LOW) when not pressed
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print("Button and LED. Press Ctrl+C to exit.")
try:
    while True:
        # Check if the button is pressed
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("Button pressed! LED ON")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        else:
            print("Button not pressed. LED OFF")
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off
        time.sleep(0.1)  # Wait 0.1 seconds to prevent bouncing

except KeyboardInterrupt:
    print("Stopping program.")
    GPIO.cleanup()