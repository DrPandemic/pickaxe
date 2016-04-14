#!/bin/python

import zmq
from threading import Thread, Condition

from protocol import compose_mining_result, parse_mining_task


context = zmq.Context()
HOST = "tcp://127.0.0.1:"
PORT = 8080
template = None
template_received = Condition()


def listening_thread():
    global template

    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    sock.connect(HOST + str(PORT))
    while True:
        template = sock.recv_json()
        with template_received:
            template_received.notify()


def submit_block(block):
    with context.socket(zmq.PUSH) as sock:
        sock.connect(HOST + str(PORT + 1))
        sock.send_string(block)


thread = Thread(target=listening_thread)
thread.start()

while True:
    if template:
        print("Working on template %s" % template["hash"])
        submit_block("my awesome block")

    else:
        print("Waiting for work from pool leader.")
        with template_received:
            template_received.wait_for(lambda: template is not None)
