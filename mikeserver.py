#!/usr/bin/python3

from flask import Flask
import socketio
import socket

JASON_HOST = "127.0.0.1"
JASON_PORT = "9000"

port = 8080

sio = socketio.Server(async_mode='threading')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

sids = {"jason": None, "client": None}

@sio.on("connect")
def connect(sid, environ):
    print("connect ", sid)

@sio.on("i_am_client")
def connect(sid, data):
    sids["client"] = sid

@sio.on("from_jason")
def from_jason(sid, data):
    sids["jason"] = sid
    sio.emit("from_jason", data, room=sids["client"])


@sio.on("from_mike_client")
def from_mike_client(sid, data):
    sio.emit("from_mike", data, room=sids["jason"])

@sio.on("disconnect")
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    app.run(threaded=True, port=port)
