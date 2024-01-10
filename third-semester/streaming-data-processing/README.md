# streaming-data-processing
### Task 1. IoT Kafka (Producers/Consumers)
---
Для запуска программы необходимо сделать следующие шаги:

1. Установить зависимости:
```
pip install -r requirements.txt
```

2. Запустить Docker-контейнер:
```
docker compose -f docker/docker-compose-kafka.yml up
```

3. Запустить код [producer.py](https://github.com/DmitryMogilnikov/streaming-data-processing/blob/main/tasks/iot_kafka/kafka/producer.py) и [consumer.py](https://github.com/DmitryMogilnikov/streaming-data-processing/blob/main/tasks/iot_kafka/kafka/consumer.py) в разных терминалах:
```
python tasks\iot_kafka\kafka\producer.py
python tasks\iot_kafka\kafka\consumer.py
```

### Task 2. Telegram Spark Streaming
---
1. Установить зависимости:
```
pip install -r requirements.txt
```

2. Ввести TG_API_ID и TG_API_HASH в [.env](https://github.com/DmitryMogilnikov/streaming-data-processing/blob/main/environments/.env) файл.
3. Запустить Telethon сессию [telethon_session.py](https://github.com/DmitryMogilnikov/streaming-data-processing/blob/main/tasks/telegram_spark_streaming/telethon_session.py):
```
python tasks/telegram_spark_streaming/telethon_session.py
```
4. Запустить код в ячейках ноутбука [tg_spark_streaming.ipynb](https://github.com/DmitryMogilnikov/streaming-data-processing/blob/main/tasks/telegram_spark_streaming/tg_spark_streaming.ipynb).
