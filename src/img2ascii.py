"""
File: main.py
Description: Convert an image to ASCII art and save it to a text file.
Author: https://github.com/jiale-wangOwO
Date: 2025-02-02
Version: 1.0
"""

import numpy as np
from PIL import Image

# Define input image, output text file, and configuration
image_path = 'assets/lenna.png' # Path to the input image
output_path = image_path.split('.')[0] + '.txt' # Path to save the output text file
ascii_chars = "MNHQ$OC?7>!:-:. "# ASCII characters sorted from dense to sparse. e.g. "MNHQ$OC?7>!:-:. ""@?>!-. "
resized_height = 255      # Height of the resized image
aspect_ratio = 1.8        # Aspect ratio of characters (height / width)

# Open and resize the image, convert it to grayscale
image = Image.open(image_path)
image_width, image_height = image.size
resized_width = int(aspect_ratio * resized_height * image_width // image_height)
image = image.resize((resized_width, resized_height), Image.Resampling.LANCZOS)
grayscale_pixels = np.array(image.convert('L'))

# Convert pixels to ASCII characters
step_size = 256 / len(ascii_chars) # For mapping pixel values to ASCII characters
ascii_art = ''
for i in range(resized_height):
    for j in range(resized_width):
        ascii_art += ascii_chars[min(int(grayscale_pixels[i][j] / step_size), len(ascii_chars) - 1)]
    ascii_art += '\n'

# Save the ASCII art to a file
with open(output_path, mode='w') as file:
    file.write(ascii_art)
