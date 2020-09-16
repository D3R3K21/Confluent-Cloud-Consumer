from kafka import KafkaProducer, KafkaConsumer
from json import loads, dumps
import ssl
from os import environ
import environment
from time import sleep
environment.initialize()
producer = KafkaProducer(bootstrap_servers= environ.get('bootstrap.servers'),
value_serializer=lambda v: dumps(v).encode('utf-8'),
sasl_mechanism='PLAIN',
security_protocol='SASL_SSL',
sasl_plain_username=environ.get('sasl.username'),
sasl_plain_password=environ.get('sasl.password'),

)

for _ in range(3):
    try:
        print('testing')
        producer.send('Test-Topic1', dumps({'test':'this out'}))
        sleep(10)
    except:
        print('error')