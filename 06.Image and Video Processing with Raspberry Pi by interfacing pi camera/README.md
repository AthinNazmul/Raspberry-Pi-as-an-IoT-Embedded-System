# **Image and Video Processing with Raspberry Pi by interfacing pi Camera**


The Raspberry Pi Camera Module is a compact, affordable camera designed for Raspberry Pi computers. It allows users to capture high-quality images and videos, making it suitable for both beginners and advanced developers. With support for multiple modes, including video and low-light photography, and programmable controls for customization, it is a flexible tool for a wide range of creative and practical projects.



You can develop many exciting projects with the Raspberry Pi camera module by just installing a camera module with your tiny pocket computer, you can explore the vast world of image processing, video processing, and even machine learning.

In this chapter, we explore how to get started with the camera module and control it using Python.

## **What you will need?** 

### **Raspberry Pi computer with a Camera Module port:**

All current models of Raspberry Pi have a port for connecting the Camera Module.

In this experiment, our exclusive focus is on the Camera Module port of the Raspberry Pi. As you have previously learned about some of the other ports , we will delve into the Camera Module port, as depicted in Figure 1\.

![Getting started with the Camera Module - What you will need | Raspberry ...][image1]

**Fig. 1:** The camera port in Raspberry Pi

**Raspberry Pi Camera Modules:** 

Raspberry Pi, the versatile single-board computer, offers a range of camera modules that have evolved over the years. These modules allow users to capture images and videos directly using the Raspberry Pi's processing power and memory. This section provides an overview of the different Raspberry Pi camera modules available.



**Raspberry Pi Camera Interface:**

The Raspberry Pi's Camera Interface offers two primary connector variants: the 15-pin and 22-pin connectors. The 15-pin connector is commonly found on standard Raspberry Pi models like the A\&B series and Pi camera modules, while the 22-pin connector is used by the Raspberry Pi Zero-W and Compute Module IO Board. Arducam also employs modified versions of these connectors to accommodate various camera board designs with different Flexible Printed Circuit (FPC) contact positions.

**15-Pin Connector:**

The 15-pin connector is the default choice for most Raspberry Pi camera applications as shown in Fig. 6\. You may encounter at least three distinct variations of the 15-pin connectors in Pi-camera-related hardware:

![][image2]

**Fig. 6:** 15-pin connector pin

Regardless of the connector model, the pinout remains consistent for these camera connectors. The following table outlines the pin definitions for the camera board, specifying whether the signals are input or output, with corresponding functions on the Raspberry Pi board:

| Pin No. | Name | Description |
| :---: | :---: | :---: |
| 1 | GND | Ground |
| 2 | CAM\_DN0 | MIPI Data Lane 0 Negative |
| 3 | CAM\_DP0 | MIPI Data Lane 0 Positive |
| 4 | GND | Ground |
| 5 | CAM\_DN1 | MIPI Data Lane 1 Negative |
| 6 | CAM\_DP1 | MIPI Data Lane 1 Positive |
| 7 | GND | Ground |
| 8 | CAM\_CN | MIPI Clock Lane Negative |
| 9 | CAM\_CP | MIPI Clock Lane Positive |
| 10 | GND | Ground |
| 11 | CAM\_IO0 | Power Enable |
| 12 | CAM\_IO1 | LED Indicator |
| 13 | CAM\_SCL | I2C SCL |
| 14 | CAM\_SDA | I2C SDA |
| 15 | CAM\_3V3 | 3.3V Power Input |

Here's a simplified summary of the pins that share the same functions:

**Data Lanes (Data Transmission):**

- CAM\_DN0 (MIPI Data Lane 0 Negative) and CAM\_DP0 (MIPI Data Lane 0 Positive): These pins form a differential pair used for transmitting image data from the camera module to the Raspberry Pi. MIPI (Mobile Industry Processor Interface) is a standardized protocol for data transfer between cameras and processors, ensuring high-speed and reliable data transmission.  
- CAM\_DN1 (MIPI Data Lane 1 Negative) and CAM\_DP1 (MIPI Data Lane 1 Positive): These pins represent an additional differential pair for transmitting image data, offering greater bandwidth and enabling the transfer of complex image information.

**Clock Lanes (Synchronization):**

- CAM\_CN (MIPI Clock Lane Negative) and CAM\_CP (MIPI Clock Lane Positive): These pins are responsible for transmitting clock signals that synchronize the data transmission between the camera module and the Raspberry Pi. Synchronization is crucial to ensure that the data is received and interpreted correctly.

**Ground Pins (Electrical Stability):**

- GND (Ground) pins: Ground pins serve as common reference points for electrical circuits. Multiple ground pins are provided to ensure stable electrical connections and to minimize noise interference.

**Power and Indicator Pins (Control):**

- CAM\_IO0 (Power Enable): This pin allows the Raspberry Pi to control the power supply to the camera module. By toggling this pin, you can turn the camera module on and off, effectively managing its power consumption.  
- CAM\_IO1 (LED Indicator): Many camera modules feature an LED indicator for signaling various states or activities, such as capturing an image or recording video. CAM\_IO1 can be used to control and interface with this indicator.

**I2C Pins (Communication):**

- CAM\_SCL (I2C Serial Clock): This pin is part of the I2C (Inter-Integrated Circuit) communication bus, and it carries the clock signal for synchronous communication between the Raspberry Pi and the camera module.  
- CAM\_SDA (I2C Serial Data): CAM\_SDA is another I2C pin responsible for transferring data between devices on the I2C bus, enabling configuration and control of the camera module.

**Power Supply (Voltage Input):**

- CAM\_3V3 (3.3V Power Input): This pin provides a regulated 3.3-volt power supply input to the camera module. It ensures that the camera module receives the necessary voltage to operate reliably and capture images or video.

**Raspberry Pi Camera Module:**

**![Raspberry Pi Camera Module][image3]**

**Fig. 7 :** Raspberry Pi Camera Module

There are two versions of the Camera Module:

* [**The standard version**](https://www.raspberrypi.org/products/camera-module-v2/)**,** which is designed to take pictures in normal light  
* [**The NoIR version**](https://www.raspberrypi.org/products/pi-noir-camera-v2/)**,** which doesn’t have an infrared filter, so you can use it together with an infrared light source to take pictures in the dark.

## **Connecting the Camera Module:**

**Let’s interface our pi camera with our raspberry Pi\!\! First, Ensure your Raspberry Pi is turned off. Now, follow the instructions below:**

1. Locate the Camera Module port.

2. Gently pull up on the edges of the port’s plastic clip.

3. Insert the Camera Module ribbon cable; make sure the connectors at the bottom of the ribbon cable are facing the contacts in the port.

4. Push the plastic clip back into place. A gif animation on how to interface pi cam is given below in Fig. 8\.

![Animation of how to connect the Raspberry Pi Camera Module][image4]

**Fig. 8:** Camera Module Connection Illustration

**Link to above gif animation:** [https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/dbf2d9575be4756f79e4293a047a8a531d340710/en/images/connect-camera.gif](https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/dbf2d9575be4756f79e4293a047a8a531d340710/en/images/connect-camera.gif)

Now, as we have interfaced our pi camera, let’s move on to the next part:

* Start up your Raspberry Pi.

* Go to the main menu and open the Raspberry Pi Configuration tool as shown in Fig. 9\.

![Raspberry Pi Configuration Tool][image5]

**Fig. 9:** Configuration tool

* Select the Interfaces tab and ensure that the camera is enabled.

![Camera enabled][image6]

**Fig. 10:** Enabling the Camera Interface

If you do not see the option “Camera”, then you need to open the terminal of your pi, then write the following line:
```
sudo raspi-config
```
  A window will appear like shown below (Fig. 11):

![][image7]

**Fig. 11:** Accessing Interface Options

* Select option 3: ‘Interface options’ and click enable camera to ‘yes’. Then, click on ‘Finish’.  
* Reboot your Raspberry Pi.

### **How to control the Camera Module via the command line:**

Now your Camera Module is connected and the software is enabled, try out the command line tools ***raspistill ***and*** raspivid.***

* Open a terminal window by clicking the black monitor icon in the taskbar (Fig. 12):

![Open terminal][image8]

**Fig. 12:** Accessing the Terminal

* Type in the following command to take a still picture and save it to the Desktop: 
``` 
raspistill \-o Desktop/image.jpg
```
![raspistill command entered into the terminal][image9]

**Fig. 13:** Taking a Photo with raspistill

* Press Enter to run the command.

When the command runs, you can see the camera preview open for five seconds before a still picture is taken.

* Look for the picture file icon on the Desktop, and double-click the file icon to open the picture.

![Image on Desktop][image10]

**Fig. 14:** Opening the Photo on the Desktop

By adding different options, you can set the size and look of the image the raspistill command takes.

* For example, add **\-h** and **\-w** to change the height and width of the image.
```   
raspistill \-o Desktop/image-small.jpg \-w 640 \-h 480  
```
* Now record a video with the Camera Module by using the following raspivid command in the terminal:
```
raspivid \-t 10000 \-o Desktop/video.h264
```
  This records a ten-second video (10,000 milliseconds) at the 1920 × 1080 resolution.

* In order to play the video file, double-click the video.h264 file icon on the Desktop to open it in VLC Media Player.

For more information and other options you can use with these commands, read the [documentation for raspistill](https://www.raspberrypi.com/documentation/accessories/camera.html) and the [documentation for raspivid.](https://www.raspberrypi.com/documentation/accessories/camera.html) If you want to see all the command for camera you can click here: [Raspberry Pi Camera Board \- RaspiStill Command List | The Pi Hut](https://thepihut.com/blogs/raspberry-pi-roundup/raspberry-pi-camera-board-raspistill-command-list)

## **How to control the Camera Module with Python code:**

The Python ***picamera*** library allows you to control your Camera Module and create amazing projects.

* Open a Python 3 editor, such as Thonny Python IDE:

![Open Thonny][image11]

**Fig. 15:** Preparing Python 3 Environment

* Open a new file and save it as ***camera.py***

*\[Note: it’s important that you never save the file as picamera.py.\]*

* Enter the following code:

```python
from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
```

* Save and run your program. The camera preview should be shown for five seconds, take an image and then close again.  
  ![Image preview][image13]

**Fig. 16:** Camera Preview

*\[Note: the camera preview only works when a monitor is connected to your Raspberry Pi. If you are using remote access (such as SSH or VNC), you won't see the camera preview.\]*

* If your preview is upside-down, you can rotate it by 180 degrees with the following code:

  `camera.rotation = 180`

* You can rotate the image by **90**, **180** or **270** degrees. To reset the image, set **rotation** to **0** degrees.

It’s best to make the preview slightly see-through so you can see whether errors occur in your program while the preview is on.

* Make the camera preview see-through by setting an **alpha** level:  
  `camera.start_preview(alpha=200)`

The **alpha** value can be any number between **0** and **255**.

*\[Note: it’s important to **sleep** for at least two seconds before capturing an image, because this gives the camera’s sensor time to sense the light levels.\]*

* Now add a loop to take five pictures in a row:
```python
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()

```
The variable **i** counts how many times the loop has run, from** 0** to **4**. Therefore, the images get saved as **image0.jpg**, **image1.jpg**, and so on.

* Run the code and hold the Camera Module in position.

The camera should take one picture every five seconds. Once the fifth picture is taken, the preview closes.

Look at your Desktop to find the five new pictures.

## **Record Video with Python:**

Now let’s record a video\!

Amend your code to remove **capture()** and instead add **start\_recording()** and **stop\_recording()**. 

Your code should look like this now:
```python
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
```
* Run the code.

Your Raspberry Pi should open a preview, record 5 seconds of video, and then close the preview.





**Reference:**

1. [Raspberry Pi Documentation \- Configuration](https://www.raspberrypi.com/documentation/computers/configuration.html)  
2. [What you will need | Setting up your Raspberry Pi | Coding projects for kids and teens](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/1)  
3. [Raspberry Pi Camera Pinout \- Arducam](https://www.arducam.com/raspberry-pi-camera-pinout/)


[image1]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/image1.png>

[image2]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/image2.png>

[image3]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/image3.png>

[image4]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/animation.gif>

[image5]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/conf1.png>

[image6]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/conf2.png>

[image7]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/conf3.png>

[image8]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/terminal.png>

[image9]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/term_bar.png>
[image10]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/desktop.png>

[image11]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/thony.png>

[image13]: <../assets/06.Image and Video Processing with Raspberry Pi by interfacing pi camera/preview.png>