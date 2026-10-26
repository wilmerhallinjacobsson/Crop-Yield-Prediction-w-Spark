#!/bin/bash

# TO RUN IT:
#   bash submit_job.sh


echo "Submitting job to spark cluster..."
docker exec bd-spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 --deploy-mode client /opt/spark-apps/test_job.py

echo "Done. Job is finished!"