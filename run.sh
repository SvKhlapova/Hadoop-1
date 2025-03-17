#! /usr/bin/env bash

OUT_DIR="streaming_wc_result"
NUM_REDUCERS=8

hadoop fs -rm -r -skipTrash $OUT_DIR*

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapred.job.name="streaming_randomIdentifiers" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper.py,reducer.py \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -input "/data/ids_part" \
    -output ${OUT_DIR} > /dev/null

hdfs dfs -cat ${OUT_DIR}/part-* | sort | head -n 50