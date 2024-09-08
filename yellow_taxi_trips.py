import pandas as pd

# Specify the file path
file_path = "/Users/Mahdi's Mac/Downloads/yellow_tripdata_2024-01.parquet"

# Load the Parquet file into a DataFrame using pyarrow
df = pd.read_parquet(file_path, engine='pyarrow')

# Display the first few rows to confirm successful loading
print(df.head())

# Display general information about the DataFrame
print(df.info())

# Summary statistics for all columns
print(df.describe())

# Focus specifically on the 'trip_distance' column
print(df['trip_distance'].describe())

# Check for any missing values in the DataFrame
print(df.isnull().sum())

# Calculate the 0.9 percentile for trip_distance
percentile_90 = df['trip_distance'].quantile(0.9)
print(f"The 0.9 percentile for trip_distance is: {percentile_90}")

# Filter the DataFrame to retain trips over the 0.9 percentile in distance
df_filtered = df[df['trip_distance'] > percentile_90]

# Display the filtered DataFrame
print(df_filtered.head())

# Check that all values in trip_distance are above the 0.9 percentile
assert df_filtered['trip_distance'].min() > percentile_90, "Some trips are below the 0.9 percentile!"

# Confirm the filtering process
print("All trips in the filtered DataFrame are above the 0.9 percentile.")


df_filtered.to_parquet("/Users/Mahdi's Mac/Downloads/filtered_yellow_tripdata_2024-01.parquet", engine='pyarrow')
