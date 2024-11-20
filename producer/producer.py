from kafka import KafkaProducer
import json
import time
import random
import os

# Kafka 설정
def create_producer():
    return KafkaProducer(
        bootstrap_servers=os.getenv('KAFKA_SERVER', 'kafka:9092'),  # Kafka 브로커 주소
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

producers = [create_producer(), create_producer()]
topic_name = 'multi-test-topic'

# 각 Producer에서 10개의 메시지를 전송
for i in range(10):
    for j, producer in enumerate(producers):
        message = {
            'producer_id': j,
            'id': i,
            'timestamp': time.time(),
            'value': random.randint(1, 100)
        }
        producer.send(topic_name, message)
        print(f"Producer {j} sent: {message}")
    time.sleep(1)

# Producer 종료
for producer in producers:
    producer.flush()
    producer.close()
