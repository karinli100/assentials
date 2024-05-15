from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def convert_and_save_image(image_path, output_path):
    """
    Converts an image to grayscale and saves it as a TIFF file, then displays the image matrix.

    Parameters:
    image_path (str): The path to the original image file.
    output_path (str): The path where the grayscale TIFF image will be saved.
    """
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Convert the grayscale image to a matrix
    img_matrix = np.array(img_gray)

    # Print the matrix
    print(img_matrix)

    # Plot the matrix as an image
    plt.imshow(img_matrix, cmap='gray')
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

    # Save the grayscale image as a TIFF file
    img_gray.save(output_path, 'TIFF')
    print(f"Image saved successfully at {output_path}")

# Example usage
image_path = 'D:/python_assentials/IMG_20220628.jpg'
output_path = 'D:/python_assentials/new_image.tiff'

convert_and_save_image(image_path, output_path)