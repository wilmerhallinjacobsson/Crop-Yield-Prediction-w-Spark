from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder \
    .appName("Test_job") \
    .getOrCreate()

# Reducing log noise
spark.sparkContext.setLogLevel("WARN")   

# Test with simple data
data = [("Alice", 34), ("Bob", 45), ("Charlie", 29)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()