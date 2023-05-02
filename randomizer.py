#!/usr/bin/env python3
#source of inspiration: https://core-electronics.com.au/guides/raspberry-pi/colour-e-ink-display-raspberry-pi/
#import all neccesary functionality
import random
import os
import signal
import RPi.GPIO as GPIO

#Create most of the text for the terminal command to change the photo and add on a random 1:10 number at the end
#a = str(random.randint(1,10))
#b = "cd /home/user/images\npython3 image.py "
#c = b + a


# Setting up button in code
BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'C', 'D']
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# "handle_button" will be called every time a button is pressed
# It receives one argument: the associated input pin.
#Whenever this function is called (thus whenever a button is clicked) it will print our image changing command to the screen
def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    print("Button press detected on pin: {} label: {}".format(pin, label))

#Press A to generate a random image path and display image
    if label == 'A':
        image_dir = "/home/user/images"
        image_path = os.path.join(image_dir, str(random.randint(1, 5)) + ".jpg")
        display_random_image = "cd /home/user/images && python3 image.py " + image_path
        os.system(display_random_image)

#Press C Button to clear the eink screen
    elif label == 'C':
        clear_screen = "cd /home/user/images && python3 clear.py"
        os.system(clear_screen)





    #os.system(c)


# Loop through out buttons and attach the "handle_button" function to each
# We're watching the "FALLING" edge (transition from 3.3V to Ground) and
# picking a generous bouncetime of 250ms to smooth out button presses.
for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=250)

# Finally, since button handlers don't require a "while True" loop,
# we pause the script to prevent it exiting immediately.
signal.pause()

