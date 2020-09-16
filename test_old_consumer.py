from kafka import KafkaProducer, KafkaConsumer
from json import loads, dumps
import ssl
from time import sleep
import environment
from os import environ

environment.initialize()

consumer = KafkaConsumer('Test-Topic1',group_id='group1',bootstrap_servers=environ.get('bootstrap.servers'),
value_deserializer=lambda m: loads(m.decode('ascii')),
sasl_mechanism='PLAIN',
security_protocol='SASL_SSL',
sasl_plain_username=environ.get('sasl.username'),
sasl_plain_password=environ.get('sasl.password'),

)

while True:
    messages = consumer.poll(max_records=1)
    
    print('messages: ',len(messages))
    if(messages=={}):
        print('none')
        sleep(3)
    else:
        message = list(messages.values())[0]
        messages = [i.value for i in message]
        # print(messages)
        for i in messages:
            print(i)