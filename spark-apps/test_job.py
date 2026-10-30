# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("DataLoading").getOrCreate()

# Reducing log noise
spark.sparkContext.setLogLevel("WARN")   


# Read Data
data = spark.read.format("csv").option("header", "true").load("data.csv")

# Cache the data in memory
data.cache()

# Count the number of records
print("Number of records: ", data.count())

# Stop SparkSession
spark.stop()