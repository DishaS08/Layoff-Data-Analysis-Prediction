import pandas as pd
import matplotlib.pyplot as plt
from data_collection import load_data
from data_cleaning import clean_data

def plot_monthly_layoffs(data):
    data.set_index('Date', inplace=True)
    data.sort_index(inplace=True)  # Ensure index is sorted
    plt.figure(figsize=(12, 6))
    data['Number_of_Layoffs'].loc['2020':'2023-12'].resample('ME').sum().plot()
    plt.title('Monthly Layoffs Trend')
    plt.xlabel('Date')
    plt.ylabel('Sum of Number of Layoffs')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = load_data('layoffs_data.csv')
    cleaned_data = clean_data(data)
    plot_monthly_layoffs(cleaned_data)
