import sys
import os
import pandas as pd
from data_collection import load_data
from data_cleaning import clean_data
from eda import plot_layoffs_over_time, plot_layoffs_by_industry
from detailed_analysis import plot_monthly_layoffs
from predictive_modeling import train_model, plot_predictions

# Add the current directory to the Python path
sys.path.append(os.path.dirname(__file__))

# Step 1: Data Collection
data = load_data('layoffs_data.csv')

# Step 2: Data Cleaning
data = clean_data(data)

# Verify columns after cleaning
print("Columns after cleaning:", data.columns)

# Step 3: EDA
plot_layoffs_over_time(data)
plot_layoffs_by_industry(data)

# Step 4: Detailed Analysis
plot_monthly_layoffs(data)

# Step 5: Predictive Modeling (Optional)
try:
    data.set_index('Date', inplace=True)
except KeyError as e:
    print(f"KeyError: {e}")

model, X_test, y_test = train_model(data)
plot_predictions(model, X_test, y_test)

