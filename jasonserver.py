#!/usr/bin/python3

import socketserver
import socketio

sio = socketio.Client()

class Buffer:
    def __init__(self):
        self.value = None

returnValue = Buffer()


@sio.on("connect")
def connect():
    print('connection established')

@sio.on("from_mike")
def from_mike(data):
    print('message received with ', data)
    returnValue.value = data["data"]

@sio.on("disconnect")
def disconnect():
    print('disconnected from server')


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        sio.emit("from_jason", {"data": self.data})

        while returnValue.value is None:
            pass

        self.request.sendall(returnValue.value)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    sio.connect('http://localhost:8080')

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
    

