#!/bin/python
import zmq
from threading import Thread
from time import sleep

context = zmq.Context()
HOST = "tcp://127.0.0.1:"
PORT = 8080
template = None

def listening_thread():
    global template

    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    sock.connect(HOST + str(PORT))
    while True:
        template = sock.recv_json()

def submit_block(block):
    with context.socket(zmq.PUSH) as sock:
        sock.connect(HOST + str(PORT + 1))
        sock.send_string(block)

thread = Thread(target=listening_thread)
thread.start()

while True:
    if template:
        print("Girl look at that body, I work out")
        submit_block("my awesome block")
        sleep(1)
    else:
        sleep(1)
