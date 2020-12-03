#!/usr/bin/python3

import socket

JASON_HOST = "127.0.0.1"
JASON_PORT = 9999

data = "Hello, world!"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((JASON_HOST, JASON_PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
