from confluent_kafka import Producer, KafkaError
import json
import ccloud_lib
from os import environ    
import uuid
def produce_message(topic, message):

    producer = Producer({
        # 'bootstrap.servers': environ.get('bootstrap.servers'),
        # 'sasl.mechanisms': environ.get('sasl.mechanisms'),
        # 'security.protocol': environ.get('security.protocol'),
        # 'sasl.username': environ.get('sasl.username'),
        # 'sasl.password': environ.get('sasl.password'),
        'bootstrap.servers': 'a310f17a6901711ea91e50a23db08089-1711275699.us-east-2.elb.amazonaws.com:19092'
    })

    # Create topic if needed
    ccloud_lib.create_topic(topic)


    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):

        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))

    for n in range(10):
        record_key = "correlationId"
        message['_id']=str(uuid.uuid4())
        record_value = json.dumps(message)
        print("Producing record: {}\t{}".format(record_key, record_value))
        producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)
        # p.poll() serves delivery reports (on_delivery)
        # from previous produce() calls.
        producer.poll(0)

    producer.flush()

