import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_cleaning import clean_data

def plot_layoffs_by_industry(data):
    sns.barplot(x='Industry', y='Number_of_Layoffs', data=data)
    plt.title('Number of Layoffs by Industry')
    plt.xlabel('Industry')
    plt.ylabel('Number of Layoffs')
    plt.xticks(rotation=45)
    plt.show()

# Load data and clean
data = pd.read_csv('layoffs_data.csv')
cleaned_data = clean_data(data)

# Debugging prints
print(cleaned_data.columns)  # Check column names
print(cleaned_data.head())   # Print first few rows to verify data

# Plotting
def plot_layoffs_over_time(data):
    plt.figure(figsize=(12, 6))  # Adjust figure size
    sns.lineplot(x='Date', y='Number_of_Layoffs', data=data, marker='o', color='b', linestyle='-')  # Adjust lineplot parameters
    plt.title('Number of Layoffs Over Time')  # Add title
    plt.xlabel('Date')  # Label for x-axis
    plt.ylabel('Number of Layoffs')  # Label for y-axis
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)  # Add grid for better visualization
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()

plot_layoffs_over_time(cleaned_data)
