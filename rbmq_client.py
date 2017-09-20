#!/usr/bin/env python3

import pika
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('rabbitmq_config.cfg')
host = config.get('attributes', 'host')
username = config.get('attributes', 'username')
password = config.get('attributes', 'password')

credentials = pika.PlainCredentials(username, password)
parameters = pika.ConnectionParameters(host,
                                   5672,
                                   '/',
                                   credentials)
connection = pika.BlockingConnectionparameters)
channel = connection.channel()
channel.queue_declare(queue='whatsnews', durable=True)

def publish(message):
	channel.basic_publish(exchange='',
        	              routing_key='whatsnews',
        	              body=message,
        	              properties=pika.BasicProperties(
        	                 delivery_mode = 2, # make message persistent
        	              ))
	print(" [x] Sent %r" % message)

