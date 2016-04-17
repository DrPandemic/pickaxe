#!/bin/python

import zmq
from threading import Thread, Condition

from protocol import compose_mining_result, parse_mining_task
from cpu_miner import mine


context = zmq.Context()
HOST = "tcp://127.0.0.1:"
PORT = 8080
pending_template = None
template = None
template_received = Condition()


def listening_thread():
    global pending_template

    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    sock.connect(HOST + str(PORT))
    while True:
        pending_template = sock.recv_json()
        print("Received block from pool leader: %s" % pending_template["hash"])
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
        task = parse_mining_task(template)

        mine(task.block, task.target)

        print("Block successfully mined!")
        serialized = task.block.serialize()
        response = compose_mining_result(serialized)

        submit_block(response)
        template = None

    else:
        print("Waiting for work from pool leader.")
        with template_received:
            template_received.wait_for(lambda: pending_template is not None)
            template = pending_template
            pending_template = None
