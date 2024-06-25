import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# TODO make hexagon fild (size) with 2 inputs   x and y
# make input as small diameter (not 2r)
# angle input as degree, not radian
def draw_hexagon(size, edge_length_m, pixel_size, rotation_angle=0):
    """
    Creates hexagon in a numpy array with a specified rotation angle.

    Parameters:
    - size (tuple): The dimensions of the numpy array (height, width).
    - edge_length_m (float): The edge length of the hexagon in meters.
    - pixel_size (float): The size of each pixel in meters.
    - rotation_angle (float): The rotation angle of the hexagon in radians.

    Returns:
    - naperture (numpy array): An array with the filled hexagon
    """
    naperture = np.zeros(size)
    center = np.array([size[1] // 2, size[0] // 2])  # center is [x, y]
    edge_in_pixels = int(edge_length_m / pixel_size)
    angle = np.pi / 3

    # Define vertices of the hexagon adjusted for horizontal orientation and rotation
    vertices = []
    for i in range(6):
        x_offset = center[0] + edge_in_pixels * np.cos(i * angle + rotation_angle)
        y_offset = center[1] + edge_in_pixels * np.sin(i * angle + rotation_angle)
        vertices.append((int(x_offset), int(y_offset)))

    # Scan-line fill for the hexagon using horizontal logic
    for x in range(size[1]):
        node_y = []
        j = 5
        for i in range(6):
            if vertices[i][0] < vertices[j][0]:
                x1, y1, x2, y2 = vertices[i][0], vertices[i][1], vertices[j][0], vertices[j][1]
            else:
                x1, y1, x2, y2 = vertices[j][0], vertices[j][1], vertices[i][0], vertices[i][1]
            if x >= x1 and x < x2:
                node_y.append((x - x1) * (y2 - y1) / (x2 - x1) + y1)
            j = i

        node_y.sort()
        for i in range(0, len(node_y), 2):
            start = int(node_y[i])
            end = int(node_y[i + 1])
            if start < end:
                naperture[start:end, x] = 1

    return naperture

def apply_hexagonal_mask(image_path, hexagon_array):
    """
    Applies a hexagonal mask to an image and displays the masked image.

    Parameters:
    - image_path (str): The path to the image file.
    - hexagon_array (numpy array): The hexagonal mask array.

    Returns:
    - masked_image (numpy array): The image with the hexagonal mask applied.
    """
    # Load an image
    image = np.array(Image.open(image_path))

    # Check if image is indeed RGB by confirming it has three dimensions
    if image.ndim == 3 and image.shape[2] == 3:
        # Extend the mask for all three channels
        mask = np.repeat(hexagon_array[:, :, np.newaxis], 3, axis=2)
    else:
        # If it's not RGB, this step should be revisited or adjusted accordingly
        mask = hexagon_array
    #Display mask
    plt.figure(figsize=(6, 6))
    plt.imshow(hexagon_array, cmap='gray', interpolation='none')
    plt.title('Filled Horizontal Hexagonal Aperture with Rotation')
    plt.show()

    # Apply the mask
    masked_image = np.where(mask == 1, image, 0)

    # Display the masked image
    plt.figure(figsize=(10, 8))
    plt.imshow(masked_image)
    plt.title('Image with Hexagonal Mask Applied')
    plt.axis('off')  # Hide axes ticks
    plt.show()

    return masked_image

# Example usage
size = (1804, 2405)  # Size of the array (height, width)
pixel_size = 0.001  # 1 mm per pixel
edge_length_m = 0.9  # 50 mm
rotation_angle = np.pi / 10  # 30 degrees in radians

# Create the hexagonal mask
hexagon_array = draw_hexagon(size, edge_length_m, pixel_size, rotation_angle)

# Apply the hexagonal mask to the image
image_path = 'IMG_20220628.jpg'
masked_image = apply_hexagonal_mask(image_path, hexagon_array)
