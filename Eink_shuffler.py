
import os
import random
from PIL import Image
from inky import InkyImpression
import time

# Set the path to the directory containing your images
image_dir = r"/home/pi/images"

# Get a list of all the image filenames in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
random.shuffle(image_files)

# Create an Inky Impression object
inky_display = InkyImpression("black")

# Set the display resolution
inky_display.set_border(inky_display.BLACK)
inky_display.resolution = (600, 800)

# Define a function to display an image
def display_image(index):
    image_path = os.path.join(image_dir, image_files[index])
    image = Image.open(image_path)
    image = image.resize((inky_display.width, inky_display.height))
    inky_display.set_image(image)
    inky_display.show()

# Set the initial image index
current_index = 0

# Set the time (in seconds) that you need to hold down the button to trigger a shuffle
shuffle_hold_time = 2

# Set the time (in seconds) between button presses to move to the next image
next_image_press_time = 0.5

# Set the initial button state to unpressed
button_pressed = False

# Set the initial shuffle flag to False
shuffle_flag = False

# Enter an infinite loop to continuously check the button state and update the display
while True:
    # Get the current time
    current_time = time.time()

    # Check if the button is pressed
    if inky_display.button_pressed:
        # Set the button_pressed flag to True
        button_pressed = True
        
        # If the shuffle_flag is True, reset the shuffle_flag and shuffle the images
        if shuffle_flag:
            shuffle_flag = False
            random.shuffle(image_files)
            current_index = 0
            display_image(current_index)
    else:
        # If the button was previously pressed and is now released, determine how long it was pressed
        if button_pressed:
            button_pressed = False
            press_duration = current_time - start_time
            
            # If the press duration was longer than the shuffle_hold_time, set the shuffle_flag to True
            if press_duration > shuffle_hold_time:
                shuffle_flag = True
            else:
                # Otherwise, move to the next image
                current_index += 1
                if current_index >= len(image_files):
                    current_index = 0
                display_image(current_index)
        
        # Sleep for a short period of time to avoid using too much CPU
        time.sleep(next_image_press_time)
