# NYC Yellow Taxi Trip Analysis

## Overview

This project analyzes the NYC Yellow Taxi trip data for January 2024. The main goal is to identify trips that exceed the 0.9 percentile in terms of distance traveled.

### Project Structure

**yellow_taxi_trips.py**: The main Python script for loading, processing, and filtering the data.

**filtered_yellow_tripdata_2024-01.csv**: The output CSV file containing trips with distances above the 0.9 percentile.

**filtered_yellow_tripdata_2024-01.parquet**: The output Parquet file containing trips with distances above the 0.9 percentile.

**README.md**: Documentation of the project.

### Approach
1. **Data Loading**: 
The script reads the Parquet file containing the January 2024 NYC Yellow Taxi trip data into a Pandas DataFrame.

2. **Data Exploration**:
The script performs basic exploration of the data, focusing on key columns like trip_distance to understand its distribution and ensure data quality.

3. **Percentile Calculation**:
The script calculates the 0.9 percentile for the trip_distance column. This percentile value acts as the threshold for filtering the data.

4. **Data Filtering**:
The DataFrame is filtered to retain only those rows where trip_distance exceeds the 0.9 percentile value.

5. **Saving the Output**:
The filtered data is saved as both a CSV and Parquet file for further review.

### Assumptions

The trip_distance column is the only metric used to filter the trips.

All trips are included in the analysis, regardless of other factors like payment type or location.

Missing values in non-relevant columns do not affect the analysis.

## How to Reproduce the Results

**Prerequisites**

Python 3.8+ installed on your system.

**Libraries:**

Pandas

PyArrow (for reading and writing Parquet files)

### Steps to Reproduce

#### Clone the Repository:


`git clone https://github.com/mahhdii/nyc-yellow-taxi-analysis.git`

`cd nyc-yellow-taxi-analysis`

### **Set Up the Environment:**

### **Create a virtual environment:**

`python3 -m venv tinybird-env`

`source tinybird-env/bin/activate`

### Install the required dependencies:

`pip install pandas pyarrow`

### **Run the Script:**

Execute the Python script to load, process, and filter the data:

`python yellow_taxi_trips.py`

### **Review the Output:**

The filtered data will be saved as **filtered_yellow_tripdata_2024-01.parquet** in your working directory.

### **Considerations for Scaling**

Data Volume: For larger datasets, consider using a distributed computing framework like PySpark.
Optimization: Loading only necessary columns and handling missing values efficiently can reduce memory usage and processing time.