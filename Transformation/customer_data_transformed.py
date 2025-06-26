import pandas as pd

# Load the customer data from the CSV file
df = pd.read_csv("customer_data.csv")

# Handle missing values (e.g., fill missing addresses with a default value)
df['address'].fillna('Unknown', inplace=True)

# Standardize address formats (e.g., convert to uppercase)
df['address'] = df['address'].str.upper()

# Print the transformed DataFrame (for demonstration purposes)
print(df.head())

# Save the transformed data to a new CSV file
df.to_csv("transformed_customer_data.csv", index=False)