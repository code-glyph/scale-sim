import os
import pandas as pd
import glob

# Define the base directory and pattern
base_dir = 'custom'
pattern = '*_*_*'

# Function to read and clean the CSV file
def read_and_clean_csv(file_path):
    df = pd.read_csv(file_path)
    # Strip leading and trailing spaces from column names
    df.columns = df.columns.str.strip()
    return df

# Function to perform aggregations and create a new DataFrame
def aggregate_data(df, config_name):
    aggregations = {
        'Total Cycles': 'sum',
        'Stall Cycles': 'sum',
        'Overall Util %': 'mean',
        'Mapping Efficiency %': 'mean',
        'Compute Util %': 'mean'
    }
    aggregated_values = df.agg(aggregations)
    aggregated_df = pd.DataFrame([aggregated_values])  # Create a single-row DataFrame
    aggregated_df.index = [config_name]  # Set the config name as the index
    aggregated_df.index.name = 'config'  # Name the index 'config'
    return aggregated_df

# Iterate through all matching directories
for directory in glob.glob(os.path.join(base_dir, pattern)):
    compute_report_path = os.path.join(directory, 'COMPUTE_REPORT.csv')
    #print(compute_report_path)
    if os.path.exists(compute_report_path):
        df = read_and_clean_csv(compute_report_path)
        config_name = os.path.basename(directory)
        aggregated_df = aggregate_data(df, config_name)
        aggregate_path = os.path.join(directory, 'aggregate.csv')
        aggregated_df.to_csv(aggregate_path)
        print(f"Created aggregate.csv in {directory}")
    else:
        print(f"COMPUTE_REPORT.csv not found in {directory}")
