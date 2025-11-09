# **Programming with Python and GPIO**

This is where the real fun begins. In this chapter, you'll learn how to write simple Python programs and use them to control and read from the Raspberry Pi's General Purpose Input/Output (GPIO) pins. This is the foundation of all IoT projects.

## **5.1 "Hello, World\!" in Python**

Python is a beginner-friendly programming language that's perfect for the Raspberry Pi. Ubuntu comes with Python pre-installed. Let's write your first script.

1. **Open your Terminal** .

In your home directory, let's create a new folder for our projects:  
mkdir Projects

2. Move into that new directory:  
   cd Projects  
3. Use `nano` to create a new Python file. We'll call it `hello.py`.  
   nano hello.py  
4. In the `nano` editor, type the following single line of code:  
   print("Hello, World\! This is my Raspberry Pi.")  
5. **Save and exit** `nano`:  
   * Press `Ctrl + X`.  
   * Press `Y` to save.  
   * Press `Enter` to confirm the filename.

Now, run your script using the `python3` command:
``` 
python3 hello.py
```
6. You should see your message printed to the terminal. **Congratulations**, you're a **Python** programmer xD\!

#### 

## **5.2 Understanding the GPIO Pins**

The **GPIO** pins are a **40-pin** header on your **Raspberry Pi** that allows it to talk to other hardware, like LEDs, sensors, and motors.

Here's what you need to know:

* **GPIO:** These are the "**general purpose**" pins you can control. They can be set as an **output** (to send a signal, like turning on an LED) or an **input** (to read a signal, like a button press).  
* **VCC (Power):** The pins provide 3.3 volts (`3V3`) and 5 volts (`5V`). These are used to provide power to your electronic components. **Warning: Never connect a 5V pin directly to a 3V3 pin or a GPIO pin, as this can permanently damage your Pi.**  
* **GND (Ground):** These are the ground pins. Any circuit you build must be connected to a GND pin to complete the circuit.

## **5.3 Installing the Necessary Python Library**

To control the GPIO pins easily with Python, we need to install a library. The most common one is `RPi.GPIO`.

1. Open your **Terminal**.

Install the library using **`apt`**. Remember from Chapter 4, we need to use **`sudo`** to install software:
```  
sudo apt update
```
```
sudo apt install python3-rpi.gpio
```

2. This will download and install the library. You're now ready to build circuits.

## **5.4 Project 1: Blinking an LED**

Our first hardware project is the "Hello, World\!" of electronics: blinking an LED.

**Hardware Needed:**

* 1 x LED (any color)  
* 1 x 330Ω Resistor (or any in the 220-330Ω range)  
* 2 x Jumper Wires  
* 1 x Breadboard

**Hardware Setup:**

1. **Safety First:** Unplug your Raspberry Pi from the power supply before connecting any wires to the GPIO pins.  
2. **LEDs have polarity:** The longer leg is the positive (anode), and the shorter leg is the negative (cathode).  
3. **Build the circuit:**

**![][image1]**

* Connect a jumper wire from a **GND** pin on the Pi to the blue (negative) rail on your breadboard.  
  * Connect the **short leg** (cathode) of the LED to this same negative rail on the breadboard.  
  * Connect the **long leg** (anode) of the LED to an empty row on the breadboard.  
  * Plug one leg of the **330Ω resistor** into the same row as the LED's long leg.  
  * Plug the other leg of the resistor into a different empty row.  
  * Connect your second jumper wire from **GPIO 17** (pin 11\) on the Pi to the row with the resistor's second leg.

**The Code:**

1. Once your circuit is built, plug your Pi back in and boot it up.  
2. Open a **Terminal**, navigate to your `Projects` folder (`cd Projects`).  
3. Create a new file: `nano blink.py`

Type (or copy) the following code into `nano`:
```python
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
```
**Execution Instructions:**

1. Save the file and exit `nano` (`Ctrl+X`, `Y`, `Enter`).

Run the script. Because it accesses hardware, you must use `sudo`:

sudo python3 blink.py

2. Look at your breadboard. Your LED should be blinking on and off every second\!  
3. To stop the program, go to your terminal and press `Ctrl + C`. The `GPIO.cleanup()` command will run, turning the LED off.

## **5.5 Project 2: Reading a Sensor (Push Button)**

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

[image1]: <../assets/04-programming-with-python-and-gpio/image1.png>