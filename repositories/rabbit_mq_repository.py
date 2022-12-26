import pika
import json

class RabbitMQRepository:
    def __init__(self, host, port, user, password, queue):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.queue = queue
        self.channel = None
    
    def openConnection(self):
        credentials = pika.PlainCredentials(self.user,self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host,self.port,'/', credentials))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def publish(self, data, routingKey):
        self.channel.basic_publish(exchange='',
                      routing_key=routingKey,
                      body=json.dumps(data))
        print("Published data to RabbitMQ")