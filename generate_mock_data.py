import pandas as pd
import numpy as np
import random
import datetime


# Generate mock data
def generate_mock_data(num_records):
    data = {
        'Date': [],
        'Company': [],
        'Industry': [],
        'Affected': []
    }

    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    for _ in range(num_records):
        random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
        company = f'Company {random.randint(1, 100)}'
        industry = random.choice(['Technology', 'Finance', 'Healthcare', 'Retail', 'Automotive'])
        affected = random.randint(10, 1000)

        data['Date'].append(random_date)
        data['Company'].append(company)
        data['Industry'].append(industry)
        data['Affected'].append(affected)

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    # Generate 1000 records of mock data
    mock_data = generate_mock_data(1000)

    # Save mock data to CSV
    mock_data.to_csv('layoffs_data.csv', index=False)
    print("Mock data generated and saved to 'layoffs_data.csv'")
