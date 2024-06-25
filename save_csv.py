import pandas as pd

# TODO make name and path separatly

def save_dataframe_to_excel(data, file_path):
    """
    Saves a given DataFrame to an Excel file.

    Parameters:
    data (dict): The data to be included in the DataFrame.
    file_path (str): The path where the Excel file will be saved.
    """
    # Create a DataFrame with the provided data
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel(file_path, index=False, engine='openpyxl')  # Ensure to use 'openpyxl' as engine

    print(f"Excel file saved successfully at {file_path}")

# Example data to save
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [28, 34, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Specify the file name to save the DataFrame
file_path = 'D:/python_assentials/new_excel_file.xlsx'

# Call the function to save the DataFrame
save_dataframe_to_excel(data, file_path)