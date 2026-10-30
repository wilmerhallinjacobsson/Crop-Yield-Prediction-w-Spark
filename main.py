import os

# Required kagglehub API key
from setup_data.data_setup import dowload_data, split_csv_into_n_parts

# Kaggle dataset id
DATASET_HANDLE = "patelris/crop-yield-prediction-dataset"
TARGET_FILE = "yield_df.csv" 

# Project directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPARK_DATA_DIR = os.path.join(BASE_DIR, "spark-data")



if __name__ == "__main__":

    # ========================================
    # 2. Manual Data Splitting Across Nodes
    # ========================================

    # Downloads the csv file from kaggle dataset
    source_file = dowload_data(url = DATASET_HANDLE, filename = TARGET_FILE)

    # Splits the csv file into 3 equal parts, creates and stores it into dirs: spark-data/ master/data_0.csv | worker1/data_1.csv | worker2/data_2.csv
    split_csv_into_n_parts(source_file, n_parts=3, base_dir= SPARK_DATA_DIR, filename='data', verbose=True)