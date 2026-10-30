#!/bin/bash
set -e

# TO RUN IT:
#   bash submit_job.sh -{JOB_FILE}.py


echo "Submitting job to spark cluster..."
docker exec bd-spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 --deploy-mode client /opt/spark-apps/$1

echo "Done. Job is finished!"