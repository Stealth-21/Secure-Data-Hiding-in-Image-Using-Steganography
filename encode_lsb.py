import cv2
import numpy as np
from PIL import Image, ImageFilter

def encode_lsb(image_path, data, apply_grayscale=False, apply_blur=False):
    if len(data) > 128:
        raise ValueError("Data exceeds 128 characters limit.")

    image = Image.open(image_path)
    
    # Apply grayscale if selected
    if apply_grayscale:
        image = image.convert('L').convert('RGB')

    # Apply blur if selected
    if apply_blur:
        image = image.filter(ImageFilter.BLUR)

    image = image.convert('RGB')
    binary_data = ''.join(format(ord(i), '08b') for i in data) + '1111111111111110'  # End marker
    data_index = 0
    data_length = len(binary_data)

    pixels = np.array(image)
    for row in pixels:
        for pixel in row:
            for channel in range(3):  # Iterate over RGB channels
                if data_index < data_length:
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary_data[data_index], 2)
                    data_index += 1
                if data_index >= data_length:
                    break

    encoded_image = Image.fromarray(pixels)
    encoded_image_path = r'C:\Cyber\steganography_project\images\encoded_image.png'
    encoded_image.save(encoded_image_path)
    return encoded_image_path