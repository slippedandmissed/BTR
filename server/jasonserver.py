#!/usr/bin/python3

import socketserver
import socketio
import sys

JASON_HOST = "127.0.0.1"
JASON_PORT = int(sys.argv[2])

MIKE_HOST = "127.0.0.1"
MIKE_PORT = int(sys.argv[1])

sio = socketio.Client()

class Buffer:
    def __init__(self):
        self.value = None

returnValue = Buffer()


@sio.on("connect")
def connect():
    print('Connected to Mike server')

@sio.on("from_mike")
def from_mike(data):
    print("Got data from Mike server: ", data)
    returnValue.value = data["data"]

@sio.on("disconnect")
def disconnect():
    print("Disconnected from Mike server")


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print("Got data from jason client {}: {}".format(self.client_address[0], self.data))

        sio.emit("from_jason", {"data": self.data})

        while returnValue.value is None:
            pass

        self.request.sendall(returnValue.value)

if __name__ == "__main__":

    print("Trying to connect to Mike server:")
    while True:
        try:
            sio.connect("http://{}:{}".format(MIKE_HOST, MIKE_PORT))
            break
        except socketio.exceptions.ConnectionError:
            pass

    with socketserver.TCPServer((JASON_HOST, JASON_PORT), MyTCPHandler) as server:
        print("Jason listening on port {}".format(JASON_PORT))
        server.serve_forever()
    

