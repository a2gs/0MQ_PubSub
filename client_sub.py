#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html
# https://pyzmq.readthedocs.io/en/latest/api/zmq.html

import sys
import zmq

if(not(len(sys.argv) == 4 or len(sys.argv) == 5 or len(sys.argv) == 7)):
	print("Usage:\n\tsys.argv[0] <SERVER> <SERVER_PORT> <TOPIC>")
	print("\tsys.argv[0] <SERVER 1> <SERVER_PORT_1> <TOPIC 1_1> <TOPIC 1_2>")
	print("\tsys.argv[0] <SERVER 1> <SERVER_PORT_1> <TOPIC 1> <SERVER 2> <SERVER_PORT_2> <TOPIC 2>\n")
	sys.exit()

hasSecondServer = False
if(len(sys.argv) == 7):
	hasSecondServer = True

hasTwoTopics = False
if(len(sys.argv) == 5):
	hasTwoTopics = True
	topic12 = sys.argv[4]

context = zmq.Context()
socket = context.socket(zmq.SUB)

server1 = sys.argv[1]
port1 = int(sys.argv[2])
topic11 = sys.argv[3]

print(f"Collecting updates from [{server1}] (1) on port [{port1}] with [{topic11}].")
socket.connect("tcp://{}:{}".format(server1, port1))
socket.setsockopt(zmq.SUBSCRIBE, topic11.encode('utf-8'))
if(hasTwoTopics == True):
	socket.setsockopt(zmq.SUBSCRIBE, topic12.encode('utf-8'))

if(hasSecondServer == True):
	server2 = sys.argv[4]
	port2 = int(sys.argv[5])
	topic2 = sys.argv[6]

	print(f"Collecting updates from [{server2}] (2) on port [{port2}] with [{topic2}].")
	socket.connect("tcp://{}:{}".format(server2, port2))
	socket.setsockopt(zmq.SUBSCRIBE, topic2.encode('utf-8'))

for update_nbr in range (15):
	string = socket.recv()
	topic, messagedata = string.split()
	print(f"Topic: [{topic}] - Msg: [{messagedata}]")
