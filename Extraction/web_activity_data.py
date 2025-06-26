import boto3
import pandas as pd
import io

# AWS credentials and S3 bucket details
aws_access_key_id = "your_aws_access_key_id"
aws_secret_access_key = "your_aws_secret_access_key"
s3_bucket_name = "your_s3_bucket_name"
s3_file_key = "website_activity.log"

try:
    # Create an S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Download the file from S3
    response = s3.get_object(Bucket=s3_bucket_name, Key=s3_file_key)
    log_data = response['Body'].read().decode('utf-8')

    # Assuming the log data is in a structured format (e.g., CSV)
    df = pd.read_csv(io.StringIO(log_data))

    # Print the DataFrame (for demonstration purposes)
    print(df.head())

except Exception as e:
    print(f"Error fetching data from S3: {e}")

# Save the DataFrame to a CSV file (optional)
df.to_csv("website_activity_data.csv", index=False)