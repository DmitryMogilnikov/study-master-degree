from pydantic import Field

from core.base_config import BaseConfig


class KafkaConfig(BaseConfig):
    kafka_topic_name: str = Field(..., env="KAFKA_TOPIC_NAME")
    bootstrap_servers: str = Field(..., env="BOOTSTRAP_SERVERS")

kafka_config = KafkaConfig()
