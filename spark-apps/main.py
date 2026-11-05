from pyspark.sql import SparkSession
from datetime import datetime

# TO RUN PIPELINE: bash submit_job.sh main.py

# inspired from https://www.dataquest.io/blog/build-your-first-etl-pipeline-with-pyspark/

# Import our ETL functions
import etl_pipeline

def main():
    """Main ETL pipeline"""

    # Track runtime
    # start_time = datetime.now()

    # Initialize Spark
    spark = etl_pipeline.create_spark_session()
    print("Spark session created")

    # Extract
    raw_df = etl_pipeline.extract_all_data(spark)
    print(f"Extracted {raw_df.count()} raw records")

    pre_df = etl_pipeline.preprocessing(spark, raw_df)
    print(f"Filtered to {pre_df.count()} during pre-processing")

    part_df = etl_pipeline.repartition(spark, pre_df)
    print(f"Extracted {part_df.count()} partitioned records")

    # Close Spark Session
    spark.stop()
    print("Spark session closed")

if __name__ == "__main__":
    main()
