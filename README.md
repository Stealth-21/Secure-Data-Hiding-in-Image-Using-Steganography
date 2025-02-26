# Secure-Data-Hiding-in-Image-Using-Steganography

**Introduction**

This project introduces a steganography tool designed to hide data within images using the Least Significant Bit (LSB) method. The tool features an intuitive interface, making it accessible for users of all skill levels. It supports a variety of image formats, including PNG, JPG, and BMP, and offers additional image processing options such as grayscale and blur. This straightforward yet effective solution allows users to securely embed messages within images, ensuring privacy and discretion.

**Key Features**

The tool is compatible with multiple image formats, providing flexibility for different use cases. Its user-friendly graphical interface simplifies the process of encoding and decoding messages. Users can apply visual effects like grayscale and blur to images, enhancing the tool's functionality. With the capacity to embed messages up to 128 characters long, it ensures accurate retrieval through the use of an end marker. The encoding process minimally impacts image quality, preserving the original appearance. Additionally, robust error management effectively handles incorrect inputs and formats, ensuring a smooth user experience.

**Functionality**

The tool offers encoding capabilities that allow users to embed messages within images, with optional grayscale or blur effects to enhance the visual presentation. Decoding functionality enables the extraction of hidden messages from encoded images, ensuring that the original data is retrieved accurately. Users can also apply visual modifications to the encoded image, providing a personalized touch to their steganographic efforts.

**Implementation Details**

To set up the tool, ensure that Python is installed on your system. Required libraries can be installed using pip, including OpenCV, NumPy, and Pillow. Once set up, the application can be launched by running main.py, which opens the graphical user interface. Users can select an image file using the "Browse" button, enter the message to encode, and click "Encode" to embed it within the image. For decoding, simply provide the path to the encoded image and click "Decode" to retrieve the hidden message. The code is organized into several components: main.py initiates the GUI, encode_lsb.py manages message embedding, decode_lsb.py handles message extraction, and gui.py provides the interface for user interaction.
