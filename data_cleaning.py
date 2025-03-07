import pandas as pd

def clean_data(data):
    # Assuming Affected directly represents layoffs for simplicity
    data['Date'] = pd.to_datetime(data['Date'])
    data['Number_of_Layoffs'] = data['Affected']
    return data



if __name__ == "__main__":
    import pandas as pd
    from data_collection import load_data

    data = load_data('layoffs_data.csv')
    cleaned_data = clean_data(data)
    print(cleaned_data.describe())
