#!/usr/bin/python3

import socketio

sio = socketio.Client()

@sio.on("connect")
def connect():
    print('connection established')
    sio.emit("i_am_client", {})

@sio.on("from_jason")
def my_message(data):
    print('message received with ', data)
    sio.emit("from_mike_client", {"data": b"Coolcool"})

@sio.on("disconnect")
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:8080')
sio.wait()
