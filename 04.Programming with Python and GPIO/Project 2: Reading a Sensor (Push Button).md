## **4.5 Project 2: Reading a Sensor (Push Button)**

Now let's try an input. We'll use a push button to turn the LED on and off.

**Hardware Needed:**

* All hardware from Project 1  
* 1 x Push Button  
* 1 x Additional Jumper Wire

**Hardware Setup:**

1. **Unplug your Pi.**  
2. Keep your LED circuit exactly as it is.  
3. Add the push button to your breadboard.  
4. Connect one leg of the button to a **3V3** pin on the Raspberry Pi.  
5. Connect the other leg of the button to **GPIO 27** (pin 13).

**The Code:**

1. Create a new file: `nano button.py`

Type the following code. Note the new `GPIO.IN` and the `if` statement.
```python
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
```

**Execution Instructions:**

1. Save and exit `nano`.

Run the script using `sudo`:

sudo python3 button.py

2. The LED should be off. Now, press and hold the button on your breadboard. The LED will light up\! Release it, and the LED will turn off.  
3. Press `Ctrl + C` to stop the program.