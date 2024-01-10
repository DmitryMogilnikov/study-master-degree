from loguru import logger


def delivery_callback(err, msg):
    if err:
        logger.error(f'ERROR: Message failed delivery: {err}')
    else:
        logger.info("Produced event to topic {topic}: key = {key} value = {value}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))