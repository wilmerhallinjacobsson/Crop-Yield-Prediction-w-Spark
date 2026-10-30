import pandas as pd
import os
import kagglehub


# Kaggle dataset id
DATASET_HANDLE = "patelris/crop-yield-prediction-dataset"
TARGET_FILE = "yield_df.csv" 

# Project directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPARK_DATA_DIR = os.path.join(BASE_DIR, "spark-data")


# --- Downloads csv file from kaggle dataset

def dowload_data(url = "patelris/crop-yield-prediction-dataset", filename = "yield_df.csv"):
    print(f"Downloading {filename} from {url} in Kaggle")
    try:
        return kagglehub.dataset_download(url, path=filename)
    except Exception as e:
        print(f"Error downloading file: {e}")
        print("Ensure Kaggle credentials are configured in ~/.kaggle/.")
        return
    

# --- Split the file into N equal parts

def split_csv_into_n_parts(original_file_name, n_parts=3, base_dir='spark-data', filename='data', has_index=True, verbose=True):
    # Count total data rows (subtract 1 for the header)
    with open(original_file_name, 'rb') as f:
        total_rows = sum(1 for _ in f) - 1

    if total_rows <= 0:
        raise ValueError("The CSV file is empty or only contains a header.")

    # Calculate exact row counts per file
    base_size, remainder = divmod(total_rows, n_parts)

    # Stream the CSV and save each chunk into its node directory
    with pd.read_csv(original_file_name, index_col=0 if has_index else None, iterator=True) as reader:
        for i in range(n_parts):
            chunk_size = base_size + (1 if i < remainder else 0)
            if chunk_size == 0:
                break

            # First part goes to 'master', subsequent parts go to 'worker1', 'worker2', etc.
            node_folder = 'master' if i == 0 else f'worker{i}'
            target_dir = os.path.join(base_dir, node_folder)

            # Create the folder structure if it doesn't exist
            os.makedirs(target_dir, exist_ok=True)

            # Build full file path (e.g., spark-data/master/data_0.csv)
            output_path = os.path.join(target_dir, f'{filename}_{i}.csv')

            chunk = reader.get_chunk(chunk_size)
            chunk.to_csv(output_path, index=False)

            if verbose:
                print(f'Successfully created {output_path} ({len(chunk)} rows)')


if __name__ == "__main__":

    # ========================================
    # 2. Manual Data Splitting Across Nodes
    # ========================================

    # Downloads the csv file from kaggle dataset
    source_file = dowload_data(url = DATASET_HANDLE, filename = TARGET_FILE)

    # Splits the csv file into 3 equal parts, creates and stores it into dirs: spark-data/ master/data_0.csv | worker1/data_1.csv | worker2/data_2.csv
    split_csv_into_n_parts(source_file, n_parts=3, base_dir= SPARK_DATA_DIR, filename='data', verbose=True)