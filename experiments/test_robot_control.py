# ssh poppy@flogo.local
# fuser -k /dev/ttyA*
# poppy-services -vv --zmq poppy-ergo-jr

import time
import random
import zmq

ROBOT = "flogo.local" # name of your robot
PORT = 5757

context = zmq.Context()
socket = context.socket(zmq.PAIR)
print ("Connecting to server...")
socket.connect("tcp://{}:{}".format(ROBOT, PORT))
print('connected')

# Florian: for speed I'd recommend 100-200
# 300 is pretty fast and 50 is super slow
socket.send_json({"robot": {"set_max_speed": {"max_speed": 60}}})
socket.send_json({"robot": {"set_compliant": {"trueorfalse": False}}})

## GET ALL MOTOR POSITIONS (6 values) AND VELOCITIES (6 values)
## IN A 12 ELEMENT ARRAY
req = {"robot": {"get_pos_speed": {}}}
socket.send_json(req)
answer = socket.recv_json()
print(answer)

## SET ALL MOTORS TO AN ANGLE (in degrees)
#req = {"robot": {"set_pos": {"positions":[10, 10, 0, 0, 0, -20]}}}
#socket.send_json(req)
#answer = socket.recv_json()

for i in range(0):
    print(i)

    ## SET ALL MOTORS TO AN ANGLE (in degrees)
    pos = [
        random.uniform(-30, 30),
        random.uniform(-20, 20),
        random.uniform(-20, 20),
        0,
        random.uniform(-20, 20),
        random.uniform(-20, 20)
    ]

    req = {"robot": {"set_pos": {"positions": pos}}}
    socket.send_json(req)
    answer = socket.recv_json()

    time.sleep(2)

socket.send_json({"robot": {"set_compliant": {"trueorfalse": True}}})
