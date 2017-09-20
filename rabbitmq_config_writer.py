#!/usr/bin/env python
import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('attributes')
config.set('attributes', 'host', '192.168.1.218')
config.set('attributes', 'username', 'user1')
config.set('attributes', 'password', 'user1')

with open('rabbitmq_config.cfg', 'wb') as configfile:
    config.write(configfile)
