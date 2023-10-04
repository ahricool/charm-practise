import kafka



def kafka_consumer():
    consumer=kafka.KafkaConsumer("kafka_demo",bootstrap_servers="127.0.0.1:9092",)

    for message in consumer:
        print("receive,key:{},value:{}".format(message.key,message.value))




kafka_consumer()