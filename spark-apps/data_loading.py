from pyspark.sql import SparkSession
# ----------------------------
# 3. Data Loading on Each Node
#-----------------------------
# Initialize Spark
spark = SparkSession.builder \
    .appName("DataLoading") \
    .getOrCreate()

# Reduce log noise
spark.sparkContext.setLogLevel("WARN")   

# Read multiple CSV files from inside the node subfolders
df = (spark.read
      .format("csv")
      .option("header", True)
      .load("/opt/spark-data/*/*.csv")  # The /*/ tells Spark to look inside master, worker1, etc.
     )

# Show the data to prove it unified successfully
df.show()
print(f"Total unified rows: {df.count()}")