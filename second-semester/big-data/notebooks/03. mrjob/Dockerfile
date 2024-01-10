FROM bigtop/sandbox:1.2.1-ubuntu-16.04-hdfs_yarn_hive_pig

RUN apt-get update && \
    apt-get install -y python3 python3-pip hadoop-httpfs

RUN service hadoop-httpfs start

RUN python3 -m pip install mrjob

COPY . /mrjob

EXPOSE 50070 14000 8088 19888 9083 10000 10002

CMD ["bash"]