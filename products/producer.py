# amqps://hkkavtfv:aM-Imqw5yuRbgr02D4W9-CVMK6hu020-@jackal.rmq.cloudamqp.com/hkkavtfv

import pika, json

params =pika.URLParameters('amqps://hkkavtfv:aM-Imqw5yuRbgr02D4W9-CVMK6hu020-@jackal.rmq.cloudamqp.com/hkkavtfv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)