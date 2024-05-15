import numpy as np
import matplotlib.pyplot as plt
#TODO: addit degree to the hexagon

def draw_filled_hexagon(size, edge_length_m, pixel_size):
    """
    Creates a filled hexagon in a numpy array.

    Parameters:
    - size (tuple): The dimensions of the numpy array (height, width).
    - edge_length_m (float): The edge length of the hexagon in meters.
    - pixel_size (float): The size of each pixel in meters.

    Returns:
    - naperture (numpy array): An array with the filled hexagon.
    """
    naperture = np.zeros(size)
    center = np.array([size[1] // 2, size[0] // 2])  # center is [x, y]
    edge_in_pixels = int(edge_length_m / pixel_size)
    angle = np.pi / 3

    # Define vertices of the hexagon
    vertices = []
    for i in range(6):
        x_offset = center[0] + edge_in_pixels * np.cos(i * angle)
        y_offset = center[1] + edge_in_pixels * np.sin(i * angle)
        vertices.append((int(x_offset), int(y_offset)))

    # Scan-line fill for the hexagon
    for y in range(size[0]):
        node_x = []
        j = 5
        for i in range(6):
            if vertices[i][1] < vertices[j][1]:
                x1, y1, x2, y2 = vertices[i][0], vertices[i][1], vertices[j][0], vertices[j][1]
            else:
                x1, y1, x2, y2 = vertices[j][0], vertices[j][1], vertices[i][0], vertices[i][1]
            if y >= y1 and y < y2:
                node_x.append((y - y1) * (x2 - x1) / (y2 - y1) + x1)
            j = i

        node_x.sort()
        for i in range(0, len(node_x), 2):
            start = int(node_x[i])
            end = int(node_x[i + 1])
            naperture[y, start:end] = 1

    return naperture


# Example usage
size = (300, 300)
pixel_size = 0.001  # 1 mm per pixel
edge_length_m = 0.05  # 50 mm
hexagon_array = draw_filled_hexagon(size, edge_length_m, pixel_size)

# Visualization
plt.figure(figsize=(6, 6))
plt.imshow(hexagon_array, cmap='gray', interpolation='none')
plt.title('Filled Hexagonal Aperture')
plt.colorbar()
plt.show()
