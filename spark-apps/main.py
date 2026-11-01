from pyspark.sql import SparkSession
import logging
import sys
import traceback
from datetime import datetime
import os

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
