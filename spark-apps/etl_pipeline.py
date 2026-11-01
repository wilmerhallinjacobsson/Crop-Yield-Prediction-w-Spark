from pyspark.sql import SparkSession
from pyspark.sql.types import *

# inspired from https://www.dataquest.io/blog/build-your-first-etl-pipeline-with-pyspark/

def create_spark_session():
    """Create a Spark session for our ETL job"""

    spark = SparkSession.builder \
        .appName("ETL_CROP_YIELD") \
        .getOrCreate()
    
    # Set the log level to reduced
    spark.sparkContext.setLogLevel("WARN")
    
    return spark


def extract_yield_data(spark, input_path):
    """Reads yield CSV file """

    print(f"Reading crop yield data from {input_path}")

    # Data schema
        # Columns: Area, Item, Year, hg/ha_yield, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp
    expected_schema = StructType([
            StructField('Area', StringType(), True),
            StructField('Item', StringType(), True),
            StructField('Year', ShortType(), True), 
            StructField('hg/ha_yield', IntegerType(), True),
            StructField('average_rain_fall_mm_per_year', FloatType() , True),
            StructField('pesticides_tonnes', FloatType(), True),
            StructField('avg_temp', FloatType() , True)
    
            ])
    
    df = spark.read.csv(
        input_path,
        header=True,
        schema=expected_schema,
        mode="PERMISSIVE" # mode=PERMISSIVE mode tells Spark to be lenient with malformed data. When it encounters rows that don't match the schema, it sets unparseable fields to null instead of crashing the entire job
    )

    print(f"Read {df.count()} rows from {input_path}")

    return df

def extract_all_data(spark):
    """Combine data from multiple sources"""

    # Read each partitioned csv file into df 
    df1 = extract_yield_data(spark, "/opt/spark-data/master/data_0.csv")
    df2 = extract_yield_data(spark, "/opt/spark-data/worker1/data_1.csv")
    df3 = extract_yield_data(spark, "/opt/spark-data/worker2/data_2.csv")

    # Unify all the df
    unified_df = df1.union(df2).union(df3)

    print(f"Unified dataset has {unified_df.count()} rows")
  
    return unified_df


