import os
import glob
import pandas as pd

# Define the base directory and pattern
base_dir = 'Resnet18'
pattern = '*_*'

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through all matching directories
for directory in glob.glob(os.path.join(base_dir, pattern)):
    aggregate_path = os.path.join(directory, 'aggregate_changebanks.csv')

    if os.path.exists(aggregate_path):
        # Read the Aggregate.csv file
        df = pd.read_csv(aggregate_path, index_col='config')
        dfs.append(df)
    else:
        print(f"Aggregate.csv not found in {directory}")

# Concatenate all DataFrames
if dfs:
    combined_df = pd.concat(dfs)

    # Save the combined DataFrame to Agg_all.csv
    output_path = os.path.join(base_dir, 'aggregateall.csv')
    combined_df.to_csv(output_path)
    print(f"Created aggregateall.csv in {base_dir}")
else:
    print("No Aggregate.csv files found")
