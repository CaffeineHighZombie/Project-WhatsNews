#!/usr/bin/env python3

import pika
import configparser

class rbmq_module:
 
  def __init__(self):
    config = configparser.ConfigParser()
    config.read('rabbitmq_config.cfg')
    host = config.get('attributes', 'host')
    username = config.get('attributes', 'username')
    password = config.get('attributes', 'password')
    self.exchange = config.get('attributes', 'exchange')
    self.queue = config.get('attributes', 'queue')
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(host,
                                       5672,
                                       '/',
                                       credentials,
                                       heartbeat=0)
    connection = pika.BlockingConnection()
    self.channel = connection.channel()
    self.channel.exchange_declare(exchange=self.exchange)
    self.channel.queue_declare(queue=self.queue, durable=True)
    self.channel.queue_bind(exchange=self.exchange,
                   queue=self.queue)

  def publish(self,message):
  	self.channel.basic_publish(exchange=self.exchange,
          	              routing_key=self.queue,
          	              body=message,
          	              properties=pika.BasicProperties(
          	              delivery_mode = 2, # make message persistent
          	              ))
  	print(" [x] Sent %r" % message)

  def subscribe(self):
    method_frame, header_frame, body = self.channel.basic_get(self.queue)
    if method_frame:
      print (method_frame, header_frame, body)
      self.channel.basic_ack(method_frame.delivery_tag)  
      return body
    else:
      return None

if __name__ == '__main__':
  rbmq_module = rbmq_module()
  for i in range(10):
    rbmq_module.publish("test")
  while(1):
    rbmq_module.subscribe()