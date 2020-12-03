#!/usr/bin/python3

import socketio
import socket
import re
import sys

APPLICATION_HOST = sys.argv[1]
APPLICATION_PORT = int(sys.argv[2])

MIKE_HOST = sys.argv[3]
MIKE_PORT = int(sys.argv[4])

PROTOCOL = None

sio = socketio.Client()

### TODO: fix
http_regex = re.compile("\\n.*?Host:.*?:\\d*.*?")

processes = {
    "http": lambda x: http_regex.sub("\nHost: {}:{}".format(APPLICATION_HOST, APPLICATION_PORT), x.decode("utf-8")).encode("utf-8")
}

def process(data):
    if PROTOCOL in processes:
        try:
            return processes[PROTOCOL](data)
        except Exception as e:
            print("ERROR WHILE PROCESSING: {}".format(e))
        finally:
            return data
    return data

@sio.on("connect")
def connect():
    print("Connected to Mike server")
    sio.emit("i_am_client", {})

@sio.on("from_jason")
def my_message(data):
    print("Received data: {}".format(data))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((APPLICATION_HOST, APPLICATION_PORT))
        processed = process(data["data"])
        print("Data to forward: {}".format(processed))
        sock.sendall(processed)

        received = sock.recv(1024)
        sio.emit("from_mike_client", {"data": received})

@sio.on("disconnect")
def disconnect():
    print('Disconnected from mike server')

while True:
    print("Trying to connect to Mike server:")
    try:
        sio.connect("http://{}:{}".format(MIKE_HOST, MIKE_PORT))
        break
    except socketio.exceptions.ConnectionError:
        pass
sio.wait()
