#!/bin/bash
set -e
# TO RUN IT:
#   bash init_spark_cluster.sh

# -- 1.2 CLUSTER RESOURCE ALLOCATION ---
export SPARK_WORKER_CPUS="1.5"
export SPARK_WORKER_MEMORY="2G"

echo "Using Resource Limits -> CPUs: $SPARK_WORKER_CPUS | RAM: $SPARK_WORKER_MEMORY"

echo "Cleaning up old containers..."
docker-compose down --remove-orphans
docker rm -f bd-spark-master bd-spark-worker-1 bd-spark-worker-2 2>/dev/null || true

echo "Building Docker containers..."
docker-compose build

echo "Starting Spark cluster..."
docker-compose up -d

echo "Done! Spark is running."