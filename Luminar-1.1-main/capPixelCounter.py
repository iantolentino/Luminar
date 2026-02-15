import cv2
from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import subprocess
import os
import time

def take_picture():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    # Capture a frame
    ret, frame = cap.read()
    # Release the camera
    cap.release()
    # Convert the OpenCV image to PIL format
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return image

def preprocess_image(image):
    # Convert the image to grayscale and enhance contrast
    enhancer = ImageEnhance.Contrast(image.convert('L'))
    enhanced_image = enhancer.enhance(2)  # Enhance contrast by factor of 2
    return enhanced_image

def count_bright_pixels(image, threshold):
    # Convert the preprocessed image to a NumPy array
    img_array = np.array(image)
    # Count bright pixels using NumPy operations
    count = np.sum(img_array >= threshold)
    return count

def adaptive_threshold(image, block_size=15, c=7):
    # Convert the image to grayscale and then to a NumPy array
    img_array = np.array(image.convert('L'))
    # Calculate local threshold using NumPy operations
    threshold_img = np.where(img_array - c >= np.mean(img_array) - c, 255, 0)
    return Image.fromarray(threshold_img.astype(np.uint8))

def main():
    while True:
        # Take a picture using the webcam
        img = take_picture()
        
        # Preprocess the image
        preprocessed_img = preprocess_image(img)
        
        # Generate adaptive threshold
        adaptive_thresh_img = adaptive_threshold(preprocessed_img)
        
        # Count bright pixels using adaptive threshold
        count = count_bright_pixels(preprocessed_img, np.mean(np.array(adaptive_thresh_img)))
        
        # Calculate total number of pixels in the image
        total_pixels = preprocessed_img.width * preprocessed_img.height
        
        # Calculate percentage of white pixels
        white_pixel_percentage = count / total_pixels
        
        # Calculate brightness level based on white pixel percentage
        brightness = int(white_pixel_percentage * 255)
        
        # Reduce brightness by a fixed amount
        reduction_amount = 40  # You can adjust this value as needed
        adjusted_brightness = max(min(brightness - reduction_amount, 255), 0)
        
        # Set the adjusted brightness
        set_brightness(adjusted_brightness)

        print("Brightness adjusted to:", adjusted_brightness)

        # Save the processed image
        save_processed_image(preprocessed_img)

        # Wait for 30 seconds before capturing the next image
        time.sleep(30)

# Function to set brightness
def set_brightness(brightness):
    # Ensure brightness is between 0 and 100
    brightness = max(min(brightness, 100), 0)
    # Set the brightness using PowerShell
    subprocess.run(["powershell", "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {})".format(brightness)])

# Function to save the processed image
def save_processed_image(image):
    # Specify the file path to save the processed image
    file_path = r"C:\Users\SampleFilePath"
    # Save the image
    image.save(file_path)

if __name__ == "__main__":
    main()
