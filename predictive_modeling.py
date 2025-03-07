from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt


def train_model(data):
    data['Month'] = data.index.month
    X = data[['Month']]
    y = data['Number_of_Layoffs']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test


def plot_predictions(model, X_test, y_test):
    predictions = model.predict(X_test)
    comparison = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
    print(comparison.head())

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions)
    plt.xlabel('Actual Layoffs')
    plt.ylabel('Predicted Layoffs')
    plt.title('Actual vs Predicted Layoffs')
    plt.show()


if __name__ == "__main__":
    from data_collection import load_data
    from data_cleaning import clean_data
    import pandas as pd

    data = load_data('layoffs_data.csv')
    cleaned_data = clean_data(data)
    cleaned_data.set_index('Date', inplace=True)

    model, X_test, y_test = train_model(cleaned_data)
    plot_predictions(model, X_test, y_test)
