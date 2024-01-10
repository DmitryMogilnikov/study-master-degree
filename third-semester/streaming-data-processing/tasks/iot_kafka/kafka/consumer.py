import os
import sys
current_dir = os.getcwd()
current_dir = f"{current_dir}/tasks/iot_kafka/"
sys.path.append(current_dir)

import json
from datetime import datetime

import pandas as pd
from confluent_kafka import Consumer
from core.kafka_config import kafka_config

consumer_conf = {
    "bootstrap.servers": kafka_config.bootstrap_servers,
    "group.id": "group10",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_conf)
consumer.subscribe([kafka_config.kafka_topic_name])


def process_iot_data(sensors_data: list[dict]) -> None:
    df_by_type = pd.DataFrame(sensors_data).groupby("sensor_type")["value"].mean().reset_index()
    df_by_name = pd.DataFrame(sensors_data).groupby("sensor_name")["value"].mean().reset_index()

    print("DataFrame по типу датчика:")
    print(df_by_type)
    print("\nDataFrame по имени датчика:")
    print(df_by_name)


def main(interval_seconds: int = 20) -> None:
    sensors_data = []
    last_processing_time = datetime.now()

    while True:
        msg = consumer.consume(num_messages=1)
        if len(msg) > 0:
            msg_value = json.loads(msg[0].value())
            sensors_data.append({
                "sensor_type": msg_value["sensor_type"],
                "sensor_name": msg_value["sensor_name"],
                "value": msg_value["value"]
            })
        
        current_time = datetime.now()
        if (current_time - last_processing_time).seconds >= interval_seconds:
            process_iot_data(sensors_data=sensors_data)
            last_processing_time=current_time
            sensors_data = []


if __name__ == "__main__":
    main()
