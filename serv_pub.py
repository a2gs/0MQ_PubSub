#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html
# https://pyzmq.readthedocs.io/en/latest/api/zmq.html

# pub.py PORT TOPIC

import zmq
import random
import sys
import time

if(len(sys.argv) != 3):
	print("Usage:\tsys.argv[0] <PORT> <TOPIC>\n")
	sys.exit()

port = int(sys.argv[1])
topic = sys.argv[2]

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:{}".format(port))

while True:
	messagedata = random.randrange(1, 100)
	msg = f"{topic} {messagedata}"
	print(msg)
	socket.send(msg.encode('utf-8'))
	time.sleep(1)
