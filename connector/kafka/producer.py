import kafka
from  kafka.errors import KafkaError

import traceback
import json

def serializer(obj):
    return json.dumps(obj).encode()

def kafka_producer():

    producer=kafka.KafkaProducer(
         bootstrap_servers=["127.0.0.1:9092"],

    )
    for i in range(0,10):
        future=producer.send(
            "kafka_demo",
            key=serializer("UID=1"),  # Same key will be sent to Same partition
            value=serializer("current:{}".format(i))
        )

        print("send {}".format(str(i)))

        try:
            future.get(timeout=10)
        except KafkaError:
            traceback.format_exc()

kafka_producer()

