import requests
import pandas as pd

# API endpoint
api_url = "https://your_ecommerce_platform.com/api/sales"

try:
    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    response.raise_for_status()

    # Parse the JSON response
    sales_data = response.json()

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(sales_data)

    # Print the DataFrame (for demonstration purposes)
    print(df.head())

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from the API: {e}")

# Save the DataFrame to a CSV file (optional)
df.to_csv("sales_data.csv", index=False)