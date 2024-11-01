import pandas as pd
import numpy as np

# Load your data
data = pd.read_csv("UAE_Companies.csv", encoding='ISO-8859-1')

# Define the first six columns
first_six_columns = data.columns[:6]

# Replace empty strings or whitespace-only strings with NaN in the first six columns
data[first_six_columns] = data[first_six_columns].replace(r'^\s*$', np.nan, regex=True)

# Drop rows where all values in the first six columns are NaN
data = data.dropna(subset=first_six_columns, how='all')

# Save the cleaned data back to a CSV if needed
data.to_csv("UAE_Companies_Cleaned.csv", index=False)

print("Rows with empty or whitespace values in the first six columns have been deleted.")
