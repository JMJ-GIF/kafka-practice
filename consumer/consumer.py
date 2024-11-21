from kafka import KafkaConsumer
import os
import json
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("KafkaConsumer")

def create_consumer(topic: str, group_id: str) -> KafkaConsumer:
    """
    Kafka Consumer 생성 함수.
    :param topic: Kafka 토픽 이름
    :param group_id: Consumer Group ID
    :return: KafkaConsumer 객체
    """
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=os.getenv('KAFKA_SERVER', 'kafka:9092'),
            group_id=group_id,
            auto_offset_reset='earliest',  # 가장 처음부터 데이터 읽기
            enable_auto_commit=True,       # 메시지 자동 커밋 활성화
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        logger.info(f"Kafka Consumer created for topic: {topic}, group_id: {group_id}")
        return consumer
    except Exception as e:
        logger.error(f"Failed to create Kafka Consumer: {e}")
        raise

if __name__ == '__main__':
    # Kafka 설정
    TOPIC = 'multi-test-topic'
    GROUP_ID = 'group_a'

    logger.info("Starting Kafka Consumer...")
    try:
        # Kafka Consumer 생성
        consumer = create_consumer(topic=TOPIC, group_id=GROUP_ID)
        logger.info(f"Listening for messages on topic '{TOPIC}' in group '{GROUP_ID}'...")
        
        # 메시지 처리
        for message in consumer:
            logger.info(f"Received message: {message.value}")
    except KeyboardInterrupt:
        logger.info("Kafka Consumer stopped manually.")
    except Exception as e:
        logger.error(f"Error in Kafka Consumer: {e}")
