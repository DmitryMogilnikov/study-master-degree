import os
import sys
current_dir = os.getcwd()
current_dir = f"{current_dir}/tasks/iot_kafka/"
sys.path.append(current_dir)

import json
import threading
import time
from datetime import datetime

import numpy as np
from confluent_kafka import Producer
from core.kafka_config import kafka_config
from utils.producer_callback import delivery_callback

producer_conf = {"bootstrap.servers": kafka_config.bootstrap_servers}
producer = Producer(producer_conf)


class SensorGenerator:
    def __init__(
            self,
            sensors_count: int,
            sensor_types: list[str],
            sensors_id_parameters: dict[str, float],
        ) -> None:
        self.sensors_count = sensors_count
        self.sensor_types = sensor_types
        self.sensors_id_parameters = sensors_id_parameters
        self.sensor_types_for_sensor_indices = {}

    def generate_random_sensor_type(self) -> str:
        return np.random.choice(self.sensor_types)

    def init_sensors(self) -> None:
        for sensor_id in range(self.sensors_count):
            sensor_type = self.generate_random_sensor_type()
            self.sensor_types_for_sensor_indices[sensor_id] = sensor_type
    
    def generate_sensor_event(self, sensor_id: int) -> str:
        event_time = datetime.utcnow().isoformat()
        sensor_name = f'sensor_{sensor_id}'
        sensor_type = self.sensor_types_for_sensor_indices[sensor_id]
        value = np.random.uniform(
            low=self.sensors_id_parameters[sensor_id]["min_value"],
            high=self.sensors_id_parameters[sensor_id]["max_value"]
        )

        return json.dumps({
            "event_time": event_time,
            "sensor_name": sensor_name,
            "sensor_type": sensor_type,
            "value": value,
        })


def generate_random_parameters(sensor_id: int) -> dict:
    min_value = np.random.uniform(-50, 50)
    max_value = np.random.uniform(0, 100) + min_value
    decay = np.random.uniform(3, (sensor_id + 1) * 3)
    return {
        "min_value": min_value,
        "max_value": max_value,
        "decay": decay,
    }


def produce_sensor_data(sensor_generator: SensorGenerator, sensor_id: int, decay: float) -> None:
    while True:
        data = sensor_generator.generate_sensor_event(sensor_id=sensor_id)
        producer.produce(
            kafka_config.kafka_topic_name,
            key=f"{sensor_id}",
            value=data,
            callback=delivery_callback,
        )
        producer.flush()
        time.sleep(decay)


def main(sensors_count: int, sensor_types: list[str], sensors_id_parameters: dict) -> None:
    threads = []

    sensor_generator = SensorGenerator(
        sensors_count=sensors_count,
        sensor_types=sensor_types,
        sensors_id_parameters=sensors_id_parameters,
    )
    sensor_generator.init_sensors()

    for sensor_id in range(sensors_count):
        thread = threading.Thread(
            target=produce_sensor_data,
            args=(
                sensor_generator,
                sensor_id, 
                sensors_id_parameters[sensor_id]["decay"],
            )
        )
        threads.append(thread)
        thread.start()
    
    
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    sensors_count = 20
    sensor_types = ["Temperature", "Pressure", "Moisture", "Electricity"]
    sensors_id_parameters = {sensor_id: generate_random_parameters(sensor_id) for sensor_id in range(sensors_count)}
    main(sensors_count=sensors_count, sensor_types=sensor_types, sensors_id_parameters=sensors_id_parameters)
