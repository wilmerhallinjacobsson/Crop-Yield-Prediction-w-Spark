# Crop Yield Prediction with Apache Spark

A collaborative university project for **Big Data Analytics on Cloud Computing Infrastructures**, leveraging containerized Apache Spark via Docker for distributed data processing and machine learning.

---

## Prerequisites

1. **Docker Desktop** (Make sure it is open and running before executing scripts).

2. (For Windows) **Git Bash / Ubuntu (WSL)**
3. (macOS/Linux) **native Unix terminal**

## Getting Started

### Dataset Setup (The raw data is not tracked in Git)

#### 1. Kaggle Credentials (One-time setup)
1. Go to [kaggle.com/settings](https://www.kaggle.com/settings).
2. Under the **API** section, click **Create New Token** (or copy your Access Token).
3. On Linux/WSL, place the token in:
```bash
   mkdir -p ~/.kaggle
   echo "YOUR_KGAT_TOKEN" > ~/.kaggle/access_token
   chmod 600 ~/.kaggle/access_token
```

#### 2. Run the Download Script
This automatically downloads the source file and partitions it into spark-data/master/ and spark-data/workerX/.
```bash
    pip install -r data-setup-requirements.txt
    python data_setup.py
    
```
---

## Spark Cluster Setup

### 1. Start the Spark Cluster

To build the containers and boot up the Spark Master and Worker nodes in the background, run:

```bash
bash spark_cluster_init.sh

```

### 2. Access the Spark Web UI

Monitor master node and active workers through the browser:

* **URL:** [http://localhost:8080](http://localhost:8080)

---

## Developing & Submitting Spark Jobs

1. **Add your code:** Place any PySpark scripts inside the `spark-apps/` folder (e.g., `test_job.py`). Because of Docker volume mounting, any file saved here is instantly available inside the container.
2. **Add your data:** Store the CSV or dataset files inside the `spark-data/` folder.
3. **Submit the job:** Run your submission script in your terminal to execute the job on the Spark cluster:
```bash
bash submit_job.sh "JOB_NAME".py

```


---

## Stopping the Cluster

When you are done, run:

```bash
docker-compose down

```
---

## Project Directory Structure

```text
Crop-Yield-Prediction-w-Spark/
│
├── spark-apps/             # PySpark scripts/jobs (bind-mounted to container)
├── spark-data/             # Partitioned datasets (bind-mounted and ignored by Git)
│   ├── master/             # Chunk 0
│   ├── worker1/            # Chunk 1
│   └── worker2/            # Chunk 2
|
|── data_setup.py           # Script to download and partition Kaggle datasets
├── docker-compose.yml      # Spark Master and Worker node definitions
├── Dockerfile              # Custom Spark image configuration (Apache Spark 3.5.0)
├── requirements.txt        # Python dependencies 
├── spark_cluster_init.sh   # Automated startup script for the cluster
├── submit_job.sh           # Automated script to submit Spark jobs to the master node
└── README.md