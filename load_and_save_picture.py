from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

def convert_and_save_image(image_path=None, excel_path=None):
    """
    Saves a grayscale image as a TIFF file and as an Excel file, displays the image matrix, and returns a DataFrame of the image matrix and the output file names.

    Parameters:
    image_path (str, optional): The path to the original image file. If not provided, a file dialog will open to select the file.
    excel_path (str, optional): The path to the Excel file containing the image matrix. If not provided, a file dialog will open to select the file.

    Returns:
    pd.DataFrame: DataFrame containing the image matrix.
    str: The path where the TIFF image was saved.
    str: The path where the Excel file was saved.
    """
    # Initialize tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select image or Excel file if path not provided
    if not image_path and not excel_path:
        file_path = filedialog.askopenfilename(
            title="Select an Image or Excel File",
            filetypes=[("All Files", "*.*"), ("Image Files", "*.tiff;*.jpg;*.jpeg;*.png"), ("Excel Files", "*.xlsx")]
        )
        if not file_path:
            print("No file selected.")
            return None, None, None
        if file_path.endswith('.xlsx'):
            excel_path = file_path
        else:
            image_path = file_path

    # Extract the directory from the input file path
    if image_path:
        input_dir = os.path.dirname(image_path)
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_image_path = os.path.join(input_dir, f"{base_name}_converted.tiff")
        output_excel_path = os.path.join(input_dir, f"{base_name}_matrix.xlsx")
        # Open the image file
        img = Image.open(image_path)
        # Convert the image to a matrix
        img_matrix = np.array(img)
    elif excel_path:
        input_dir = os.path.dirname(excel_path)
        base_name = os.path.splitext(os.path.basename(excel_path))[0]
        output_image_path = os.path.join(input_dir, f"{base_name}_converted.tiff")
        output_excel_path = os.path.join(input_dir, f"{base_name}_matrix.xlsx")
        # Read the Excel file
        df = pd.read_excel(excel_path, header=None)
        # Convert DataFrame to a numpy array (image matrix)
        img_matrix = df.to_numpy()

    # Create a DataFrame from the image matrix
    df = pd.DataFrame(img_matrix)

    # Plot the matrix as an image
    plt.imshow(img_matrix, cmap='gray')
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

    # Save the image as a TIFF file
    img = Image.fromarray(img_matrix.astype('uint8'))
    img.save(output_image_path, 'TIFF')
    print(f"Image saved successfully at {output_image_path}")

    # Save the DataFrame as an Excel file
    df.to_excel(output_excel_path, index=False, header=False)
    print(f"Image matrix saved successfully at {output_excel_path}")

    return df, output_image_path, output_excel_path

# Example usage
image_path = None  # Set to None to use file dialog
excel_path = None  # Set to None to use file dialog

df, saved_image_path, saved_excel_path = convert_and_save_image(image_path=image_path, excel_path=excel_path)
if df is not None:
    print("DataFrame of image matrix:")
    print(df)
    print(f"Saved image file path: {saved_image_path}")
    print(f"Saved Excel file path: {saved_excel_path}")




exit()


##################################################################################
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#TODO we will not get RJB
# make input as path or brouth, downlod csv or tiff
# output as dataframe and name of the file

def convert_and_save_image(image_path, output_path):
    """
    Converts an image to grayscale and saves it as a TIFF file, then displays the image matrix.

    Parameters:
    image_path (str): The path to the original image file.
    output_path (str): The path where the grayscale TIFF image will be saved.
    """
    # Open the image file
    img = Image.open(image_path)

    # Convert the grayscale image to a matrix
    img_matrix = np.array(img)

    # Print the matrix
    print(img_matrix)

    # Plot the matrix as an image
    plt.imshow(img_matrix, cmap='gray')
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

    # Save the grayscale image as a TIFF file
    img.save(output_path, 'TIFF')
    print(f"Image saved successfully at {output_path}")
    return img_matrix

# Example usage
image_path = 'D:/python_assentials/new_image.tiff'
output_path = 'D:/python_assentials/new_image1.tiff'

convert_and_save_image(image_path, output_path)