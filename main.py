import matplotlib.pyplot as plt  # For plotting and displaying images
import cv2  # OpenCV library for image processing
import numpy as np  # NumPy for numerical operations on arrays
import requests  # For making HTTP requests to fetch the image
from io import BytesIO  # For handling byte data
from PIL import Image  # PIL (Pillow) for image handling

# Fetch image from URL (example URL)
url = "https://banner2.cleanpng.com/20180811/exl/kisspng-television-show-princess-carolyn-bojack-s-theme-bo-sticker-de-paulakheyides-sur-other-bojack-horseman-5b6ec4e2f35e57.4247117415339860189969.jpg"  # Put a valid image URL here
response = requests.get(url)

# Load the image and display an error message if it fails
try:
    img = Image.open(BytesIO(response.content))
    image = np.array(img)
except Exception as e:
    print("Image could not be loaded:", e)
    exit()

# Pixelation function
def pixelate(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # Resize down
    small_image = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)

    # Resize up
    pixelated_image = cv2.resize(small_image, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)
    
    return pixelated_image

# Pixelation level (percentage)
scale_percent = 10

# Create the pixelated image
pixelated_image = pixelate(image, scale_percent)

# Function to add text to the image
def add_text_to_image(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White color
    thickness = 2
    size = cv2.getTextSize(text, font, font_scale, thickness)[0]

    # Position where the text will be placed
    x = (image.shape[1] - size[0]) // 2
    y = image.shape[0] - 20

    # Add the text
    cv2.putText(image, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

    return image

# Add the text
text = "By Mahir Teymurlu"
pixelated_image_with_text = add_text_to_image(pixelated_image.copy(), text)

# Display the result
plt.figure(figsize=(10, 10))
plt.imshow(pixelated_image_with_text)
plt.axis('off')
plt.show()
