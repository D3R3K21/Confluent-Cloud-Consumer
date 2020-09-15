    

def produce_message(topic):

    producer = Producer({
        'bootstrap.servers': environ.get('bootstrap.servers'),
        'sasl.mechanisms': environ.get('sasl.mechanisms'),
        'security.protocol': environ.get('security.protocol'),
        'sasl.username': environ.get('sasl.username'),
        'sasl.password': environ.get('sasl.password'),
    })

    # Create topic if needed
    ccloud_lib.create_topic(topic)

    delivered_records = 0

    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):
        global delivered_records
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            delivered_records += 1
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))

    for n in range(10):
        record_key = "correlationId"
        record_value = json.dumps({'count': n})
        print("Producing record: {}\t{}".format(record_key, record_value))
        producer.produce(topic, key=record_key, value=message, on_delivery=acked)
        # p.poll() serves delivery reports (on_delivery)
        # from previous produce() calls.
        producer.poll(0)

    producer.flush()

    print("{} messages were produced to topic {}!".format(delivered_records, topic))
