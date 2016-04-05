import zmq
import sys

context = zmq.Context()

if sys.argv[1] == "pull":
    sock = context.socket(zmq.PULL)
    sock.connect("tcp://127.0.0.1:3000")

    message = sock.recv()
    print(message)

elif sys.argv[1] == "push":
    sock = context.socket(zmq.PUSH)
    sock.bind("tcp://127.0.0.1:3000")
    sock.send_json({"wow":42})

elif sys.argv[1] == "sub":
    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    sock.connect("tcp://127.0.0.1:3000")

    for i in range(1,10):
        message = sock.recv()
        print(message)
