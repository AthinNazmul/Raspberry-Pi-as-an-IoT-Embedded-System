# **Object Detection Using Raspberry Pi:**

**![][image1]**  
**Fig. 18:** Object detection algorithm running on Raspberry Pi

Now that you know how to set up and use the camera module in Raspberry Pi, it’s time to use it for something more interesting\!

Did you know that we can use the processing power of Raspberry pi to run Machine Learning algorithms? For instance, we may run an established object detection algorithm based on ML that runs onboard the raspberry Pi that can detect around 80 common objects\! 


After you are done, your raspberry pi should be able to detect 80 common household objects (and even a human) as shown in Fig. 18\. 

## **Introduction:**

As you should have already guessed, we will be using Python for implementing and deploying our object detection model. The great thing about working with python for ML is that we may use many built-in libraries and functions to make our life easier\!  

For this task, we’ll need the following: 

**Tensorflow Lite:** TensorFlow Lite is an open-source deep learning framework developed by Google that is designed for mobile and embedded devices (for instance, our raspberry Pi). It is a lightweight version of the popular deep learning framework TensorFlow, optimized for resource-constrained platforms

**OpenCV**: OpenCV, or Open Source Computer Vision Library, is an open-source computer vision and machine learning software library. We’ll use this library to parse the images from the Pi camera’s video and feed it to our object detection algorithm. 

**Raspberry Pi:** Obviously, we’ll need your favorite new single-board computer, Raspberry Pi to run the object detection model\! 

**Pi cam:** To get live video feed from the environment. 

We’ll also need various other python libraries that we’ll get to in time. No need to worry about their particular use, for now. 

## **Now, let’s get started\! Steps we need to follow is given below:**

![][image2]

### **Step 1: Update the Raspberry Pi**

First, we’ll need to update our Pis to the latest software version. For this, open command Prompt in your Pi (keyboard shortcut **CTRL+ALT+T**) and issue the following commands. 
```
sudo apt-get update 
sudo apt-get dist-upgrade
```

### **Step 2: Download the Code Repository**

Another great aspect of coding ML with python is that you’ll get a lot of open source resources. For this, we’ll use a github repository by EdjeElectronics. The repository contains scripts we'll use to run TensorFlow Lite, as well as a shell script that will make installing everything else we’ll need easier. For this issue, the following command is in the same terminal. 
```
git clone  https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
```
This will download everything we need into a folder called “TensorFlow-Lite-Object-Detection \-on-Android-and-Raspberry-Pi”. Since the folder name is a little too long, let’s rename it “objDetection” and then let’s browse into that directory using our command promt so that we can work with the files inside. For this, issue the following commands, 
```
mv TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi objDetection 
cd objDetection
```
You should be familiar with these linux commands. “mv” is used here to rename the folder and “cd” is used to change directory to the newly renamed “objDetection” folder. 

### **Step 3: Create a virtual environment in our Pi**

In Linux, a virtual environment is a self-contained and isolated environment within which you can install and manage software packages and libraries independently of the system-wide packages. Virtual environments are particularly useful when you're working on multiple projects with different software requirements, and you want to avoid conflicts or dependencies on the system-wide software. They are commonly used in Python development.

Now, if all that was a little too hard to grasp, think of virtual environments as rooms in your home. You keep all the furniture you need for dining in your dining room so that you can dine there, right? Likewise, you have different rooms with different furniture for different work/purposes. 

Think of the rooms as virtual environments, the furniture as necessary python libraries/ dependencies and the purpose of our virtual “room” is object detection\!   
For this let’s first install virtualenv in our Pi, with the following command: 
```
sudo pip3 install virtualenv
```

Then, let’s create a new virtual environment (or a new room\!) for our object detection model, 
```
python3 \-m venv objDetection-env
```
This will create a folder called objDetection-env inside the objDetection directory. The objDetection-env folder will hold all the package libraries for this environment. 

Next, we’ll have to activate the environment by issuing:
```
source objDetection-env/bin/activate
```
**NOTE:** You'll need to issue the source objDetection-env/bin/activate command from inside the /home/pi/objDetection (or wherever you’ve kept the git repository) directory to reactivate the environment every time you open a new terminal window (or you’ve shut down your Pi). 

You can tell when the environment is active by checking if (objDetection-env) appears before the path in your command prompt.

### **Step 4: Install TensorFlow Lite and OpenCV**

Next, let’s install TensorFlow, OpenCV, and all other dependencies needed for the object detection mofel. OpenCV is not needed to run TensorFlow Lite, but the object detection scripts in this repository use it to grab images and draw detection results on them.

All the necessary requirements are given inside the “get\_pi\_requirements.sh” script. So, if we just run this shell script we should be good\!

However, note that, just like time, python versions are always changing and you may need additional requirements. For instance, we’ll need an additional library that isn’t inside the git repository script. 

Simply, add the command (sudo apt-get install libopenblas-dev) inside the “get\_pi\_requirements. sh”  script or give it in the terminal window after running the “get\_pi\_requirements.sh” script. 

For this, run the following commands, 
```
bash get\_pi\_requirements.sh sudo apt-get install libopenblas-dev pip uninstall numpy pip install numpy==1.26.4
```
This downloads about 400MB worth of installation files, so it may take a while. 

**NOTE**: If you get an error while running the bash get\_pi\_requirements.sh command, it's likely because your internet connection timed out, or because the downloaded package data was corrupted. If you get an error, try re-running the command a few more times.

### **Step 5: Set Up/Deploy the TensorFlow Lite Object Detection model**

Now that we’re done installing all necessary python libraries and downloading necessary git repositories, it’s time to import the model itself\!

**We’ll be using an already trained object detection model that can detect 80 objects** ([**here’s**](https://gist.github.com/AruniRC/7b3dadd004da04c80198557db5da4bda) **the list of objects this model can detect with class number**). This model is provided by Google. It’s a sample quantized SSDLite-MobileNet-v2 object detection model which is trained off the MSCOCO dataset and converted to run on TensorFlow Lite. 

If you didn’t understand all that, just note that we’ll be using a model provided by google. We may also design/tweak our own model later (preferably after you do ML/DIP courses)\! 

Next, let’s install TensorFlow, OpenCV, and all other dependencies needed for the object detection model. OpenCV is not needed to run TensorFlow Lite, but the object detection scripts in this repository use it to grab images and draw detection results on them.

We can download this model using the command:
```
wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco\_ssd\_mobilenet\_v1\_1.0\_quant\_2018\_06\_29.zip
```

Then, unzip it to a folder called "Sample\_TFLite\_model" by issuing (this command automatically creates the folder):
```
unzip coco\_ssd\_mobilenet\_v1\_1.0\_quant\_2018\_06\_29.zip \-d Sample\_TFLite\_model
```
Now, it’s finally time to run the model\! 

First, check once again, that Pi cam is working properly (as per previous tutorial). Then, run the   
TFLite\_detection\_webcam.py (downloaded from the git repository we imported) by simply issuing the following command:
```
python3 TFLite\_detection\_webcam.py \--modeldir=Sample\_TFLite\_model
```

**If you’ve done everything correctly**, after a few moments of initializing, a window will appear showing the webcam feed. Detected objects will have bounding boxes and labels displayed on them in real time. 

**But what if you’ve made some mistakes? Check out the common errors you may face at the end of this guide. Should help you resolve the errors.**  

## **Further Work:** 

Now that we’ve done some fun stuff with Raspberry Pi, let’s get a little more comfortable\! We can do some amazing things with a bit of python coding\!

**Option A: Make changes to an actuator/motor when you detect a certain object**

Let’s say you want to turn on an LED light when a human approaches your Pi cam. We can just add a bit of code inside the “**TFLite\_detection\_webcam.py**” inside our /home/pi/objDetection (or wherever you’ve kept the git repository) directory. 

Humans are detected as **class number “1” ([here’s](https://gist.github.com/AruniRC/7b3dadd004da04c80198557db5da4bda)** the list of all classes) in our object detection model. 



**Option B: Make your own model that can detect a custom object which is not included in the 80 objects in the MSCOCO dataset.** 

As mentioned before. This is a bit more challenging if you haven’t completed ML/DIP courses. You may not fully understand (conceptually) what you’re doing. However, if you’re interested, I recommended checking out the following resources:

1.  Train, export, and deploy a TensorFlow Lite object detection model on the Raspberry Pi: [Link](https://www.youtube.com/watch?v=XZ7FYAMCc4M) [How to Train TensorFlow Lite Object Detection Models Using Google Colab  |  SSD MobileNet](https://www.youtube.com/watch?v=XZ7FYAMCc4M)

2. Custom Model Training with TensorFlow Lite: [Link](https://www.youtube.com/watch?v=-ZyFYniGUsw)  
    [Train a custom object detection model using your data](https://www.youtube.com/watch?v=-ZyFYniGUsw)

In this case, you’ll end up with a different model. So, since our model will have a different name than "Sample\_TFLite\_model", we’ll use that name instead. For example, I would use \--modeldir=My\_Custom\_Model\_model to run my custom object detection model in **Step 5**. Step 1-4 will remain the same (you won;t need to do them again\!, simply set up and deploy your new model to Pi).

## **Common Errors:** 

**1\. TypeError:** int() argument must be a string, a bytes-like object or a number, not 'NoneType'  
The 'NoneType' error means that the program received an empty array from the webcam, which typically means something is wrong with the webcam or the interface to the webcam. Try plugging and re-plugging the webcam a few times, and/or power cycling the Raspberry Pi, and see if that works. If not, you may need to try using a new webcam.

**2\. ImportError: No module named 'cv2'**  
This error occurs when you try to run any of the TFLite\_detection scripts without activating the 'tflite1-env' first. It happens because Python cannot find the path to the OpenCV library (cv2) to import it.

Resolve the issue by closing your terminal window, re-opening it, and issuing:
```
cd objDetection  
source objDetection-env/bin/activate  
```
Then, try re-running the script as described in **Step 5**.

**3\. These Packages Do Not Match The Hashes From The Requirements File**  
This error can occur when you run the bash get\_pi\_requirements.sh command in Step 1c. It occurs because the package data got corrupted while downloading. You can resolve the error by re-running the bash get\_pi\_requirements.sh command a few more times until it successfully completes without reporting that error.

**4\. Unsupported data type in custom op handler: 6488064Node number 2 (EdgeTpuDelegateForCustomOp) failed to prepare.**  
This error occurs when trying to use a newer version of the libedgetpu library (v13.0 or greater) with an older version of TensorFlow (v2.0 or older). It can be resolved by uninstalling your current version of TensorFlow and installing the latest version of the tflite\_runtime package. Issue these commands (make sure you are inside the tflite1-env virtual environment):
```
pip3 uninstall tensorflow  
pip3 install https://dl.google.com/coral/python/tflite\_runtime-2.1.0.post1-cp37-cp37m-linux\_armv7l.whl  
```
(Or, if you're using Python 3.5, use pip3 install https://dl.google.com/coral/python/tflite\_runtime-2.1.0.post1-cp35-cp35m-linux\_armv7l.whl instead.)

Then, re-run the TFLite detection script. It should work now\!

Note: the URLs provided in these commands may change as newer versions of tflite\_runtime are released. Check the TFLite Python Quickstart page for download URLs to the latest version of tflite\_runtime.

**5\. IndexError: list index out of range**  
This error usually occurs when you try using an "image classification" model rather than an "object detection" model. Image classification models apply a single label to an image, while object detection models locate and label multiple objects in an image. The code in this repository is written for object detection models.

Many people run into this error when using models from Teachable Machine. This is because Teachable Machine creates image classification models rather than object detection models. To create an object detection model for TensorFow Lite, you'll have to follow the guide in this repository.

If you'd like to see how to use an image classification model on the Raspberry Pi, please see this example: [https://github.com/tensorflow/examples/tree/master/lite/examples/image\_classification/raspberry\_pi](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi)






[image1]: <../assets/07. Running a Pre-trained Object Detection Model/animation.gif>

[image2]: <../assets/07. Running a Pre-trained Object Detection Model/image2.png>

