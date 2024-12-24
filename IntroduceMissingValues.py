import pandas as pd
import numpy as np

# Set the percentage of missing values you want
missing_percentage = 0.05  # 5% of the total dataset

# Exclude 'Patient Id' column and index from introducing missing values
columns_to_consider = df.columns.difference(['Patient Id'])
total_values = len(df) * len(columns_to_consider)
num_missing = int(total_values * missing_percentage)

# Set a seed for reproducibility
np.random.seed(42)

# Randomly select indices to set as NaN
missing_indices = [
    (np.random.randint(0, len(df)), np.random.choice(columns_to_consider))
    for _ in range(num_missing)
]

# Introduce NaN values at the selected indices
for row, col in missing_indices:
    df.at[row, col] = np.nan

# Save the modified dataframe
df.to_csv("lung_dataset_with_missing_values.csv", index=True)

print(df)