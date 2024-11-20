from kafka import KafkaConsumer
import json
import os
import threading

# Kafka 설정
def create_consumer(group_id):
    return KafkaConsumer(
        'multi-test-topic',
        bootstrap_servers=os.getenv('KAFKA_SERVER', 'kafka:9092'),  # Kafka 브로커 주소
        group_id=group_id,  # Consumer 그룹 설정
        auto_offset_reset='earliest',  # 가장 처음부터 데이터 읽기 시작
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

# Consumer 그룹 A와 B 생성
def consume_messages(consumer_id, group_id):
    consumer = create_consumer(group_id)
    print(f"Consumer {consumer_id} in Group {group_id} listening for messages...")
    for message in consumer:
        print(f"Consumer {consumer_id} in Group {group_id} received: {message.value}")

# 각 Consumer를 별도의 스레드에서 실행
threads = []
for i in range(2):
    t = threading.Thread(target=consume_messages, args=(f'1-{i}', 'group_a'))
    threads.append(t)
    t.start()

for i in range(2):
    t = threading.Thread(target=consume_messages, args=(f'2-{i}', 'group_b'))
    threads.append(t)
    t.start()

# 모든 스레드가 종료될 때까지 대기
for t in threads:
    t.join()
