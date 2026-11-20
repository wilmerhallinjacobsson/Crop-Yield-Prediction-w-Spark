from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression, RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator



"""
The Machine Learning pipeline should inclide:

- Feature Transformations (scaling, vectorization, etc.)

- Model Training (e.g., Linear Regression, Random Forest, etc.)

- Model evaluation (e.g., RMSE, R2, etc.)
"""

