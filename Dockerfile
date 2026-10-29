# For Spark 3.5 with Python3, Java 11, and Scala 2.12 on Ubuntu
# (note this is not the latest spark image)
FROM apache/spark:3.5.0-scala2.12-java11-ubuntu

USER root

# Install Python
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark
RUN pip3 install pyspark

# Set Python environment variables
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

USER spark
WORKDIR /opt/spark