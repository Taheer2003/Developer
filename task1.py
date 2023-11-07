import pandas as pd
import random

# Generate synthetic data
data = {
    'Name': [f'Person {i}' for i in range(1, 11)],
    'Age': [random.randint(18, 60) for _ in range(10)],
    'Salary': [random.randint(30000, 90000) for _ in range(10)],
    'City': [random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']) for _ in range(10)]
}

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('synthetic_data.csv', index=False)

print("CSV dataset created and saved as 'synthetic_data.csv'")