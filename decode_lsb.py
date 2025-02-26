from PIL import Image
import numpy as np

def decode_lsb(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    binary_data = ''

    pixels = np.array(image)
    for row in pixels:
        for pixel in row:
            for channel in range(3):
                binary_data += format(pixel[channel], '08b')[-1]

    # Split by 8 bits and stop at the end marker
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ''
    for byte in all_bytes:
        if byte == '11111111':  # End marker
            break
        decoded_data += chr(int(byte, 2))
    return decoded_data