# Required kagglehub API key
from data_split.manual_data_splitting import dowload_data, split_csv_into_n_parts


if __name__ == "__main__":

    # ========================================
    # 2. Manual Data Splitting Across Nodes
    # ========================================

    # Downloads the yield_df.csv file from crop-yield-prediction-dataset on kaggle
    source_file = dowload_data(url = "patelris/crop-yield-prediction-dataset", filename = "yield_df.csv")

    # Splits the csv file into 3 equal parts in dirs spark-data/ master/data_0.csv | worker1/data_1.csv | worker2/data_2.csv
    split_csv_into_n_parts(source_file,n_parts=3, base_dir='spark-data', filename='data', verbose=True)