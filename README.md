# Phase 1 Project 
## Team Members- Preya Patel, Sai Srikar

## Overview
This project processes a Twitter dataset to extract hashtags and URLs and perform WordCount using Apache Hadoop and Apache Spark on the FABRIC testbed.

The pipeline includes:
1. Extracting hashtags and URLs from JSON tweets
2. Running WordCount using Hadoop MapReduce
3. Running WordCount using Spark

---

## Project Directory Structure

```
~/phase1_project
│
├── code/
│   ├── extract_hashtags.py
│   └── extract_urls.py
│
├── data/
│   ├── tweets_original_data.json
│   ├── hashtags.txt
│   └── urls.txt
│
├── logs/
│   ├── hadoop_hashtags_log.txt
│   └── hadoop_urls_log.txt
│
└── wordcount_output/
    ├── wordcount_hadoop_hashtags/
    ├── wordcount_hadoop_urls/
    ├── wordcount_spark_hashtags/
    └── wordcount_spark_urls/
```

---

## Requirements

- Ubuntu VM on FABRIC
- Hadoop installed and configured
- Spark installed and configured
- Python 3

---

## Step 1 – Extract Hashtags and URLs

The dataset file must be placed in:

```
~/phase1_project/data/tweets_original_data.json
```

Run extraction scripts from the `code` directory.

### Extract hashtags

```bash
cd ~/phase1_project/code
python3 extract_hashtags.py
```

Output file:

```
~/phase1_project/data/hashtags.txt
```

### Extract URLs

```bash
python3 extract_urls.py
```

Output file:

```
~/phase1_project/data/urls.txt
```

---

## Step 2 – Run Hadoop WordCount

Upload files to HDFS:

```bash
hdfs dfs -put data/hashtags.txt /phase1_project/
hdfs dfs -put data/urls.txt /phase1_project/
```

Run Hadoop WordCount:

```bash
hadoop jar hadoop-mapreduce-examples.jar wordcount /phase1_project/hashtags.txt /phase1_project/wordcount_hashtags
hadoop jar hadoop-mapreduce-examples.jar wordcount /phase1_project/urls.txt /phase1_project/wordcount_urls
```

Copy output back to local directory if needed:

```bash
hdfs dfs -get /phase1_project/wordcount_hashtags ~/phase1_project/wordcount_output/
hdfs dfs -get /phase1_project/wordcount_urls ~/phase1_project/wordcount_output/
```

View top results:

```bash
sort -k2 -nr part-r-00000 | head -10
```

---

## Step 3 – Run Spark WordCount

Start Spark from the project directory:

```bash
cd ~/phase1_project
spark-shell
```

### Hashtags WordCount

```scala
val counts = sc.textFile("data/hashtags.txt").map(x => (x,1)).reduceByKey(_+_)
counts.saveAsTextFile("wordcount_spark_hashtags")
```

### URLs WordCount

```scala
val counts = sc.textFile("data/urls.txt").map(x => (x,1)).reduceByKey(_+_)
counts.saveAsTextFile("wordcount_spark_urls")
```

Exit Spark:

```scala
:quit
```

Spark output folders appear in:

```
~/phase1_project/wordcount_output/
```

View top results:

```bash
cat part-* | sort -t, -k2 -nr | head -10
```

---

## Step 4 – Logs

Hadoop execution logs are stored in:

```
~/phase1_project/logs/
```

These logs contain MapReduce execution information and job completion details.

---

## Summary

This project demonstrates a full processing workflow:

- JSON parsing using Python
- Distributed processing using Hadoop MapReduce
- In-memory distributed processing using Spark

Both Hadoop and Spark can be used to process the same dataset with comparable results.
