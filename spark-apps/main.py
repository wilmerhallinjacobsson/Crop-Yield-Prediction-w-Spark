from pyspark.sql import SparkSession
from datetime import datetime
import os

# TO RUN PIPELINE: bash submit_job.sh main.py

# Import our ETL functions
from etl_pipeline import *

def main():
    """Main ETL pipeline"""

    # Track runtime
    # start_time = datetime.now()

    # Initialize Spark
    spark = create_spark_session()
    print("Spark session created")

    # Extract
    raw_df = extract_all_data(spark)
    print(f"Extracted {raw_df.count()} raw records")


    # Close Spark Session
    spark.stop()
    print("Spark session closed")

if __name__ == "__main__":
    main()
