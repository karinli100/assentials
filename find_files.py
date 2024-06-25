import os
# TODO add vector with only names of the files
def find_files(directory, file_extension):
    """
    Finds all files with the specified extension in the given directory and its subdirectories.

    Parameters:
    directory (str): The directory to search within.
    file_extension (str): The file extension to look for (e.g., '.png').

    Returns:
    list: A list of paths to the files with the specified extension.
    """
    # List to store the paths of files with the specified extension
    matching_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(file_extension.lower()):
                matching_files.append(os.path.join(root, file))

    return matching_files

# Specify the directory to search
directory = 'D:\\python_assentials'

# Specify the file extension to look for
file_extension = 'png'

# Get the list of files with the specified extension
files = find_files(directory, file_extension)

# Print the list of files
for file in files:
    print(file)