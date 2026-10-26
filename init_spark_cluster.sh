#!/bin/bash

# TO RUN IT:
#   bash init_spark_cluster.sh

echo "Cleaning up old containers..."
docker-compose down

echo "Building Docker containers..."
docker-compose build

echo "Starting Spark cluster..."
docker-compose up -d

echo "Done! Spark is running."