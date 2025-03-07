import pandas as pd
import os


def load_data(file_name):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


if __name__ == "__main__":
    file_name = 'layoffs_data.csv'
    data = load_data(file_name)

    if data is not None:
        print(data.head())
import pandas as pd
import os


def load_data(file_name):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


if __name__ == "__main__":
    file_name = 'layoffs_data.csv'
    data = load_data(file_name)

    if data is not None:
        print(data.head())
