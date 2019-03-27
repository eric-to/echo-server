#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  # s.sendall(b'Hello, world')
  # data = s.recv(1024)

  message = input(" -> ")
  while True:
    s.send(message.encode())
    data = s.recv(1024).decode()
    print('Received from server: ' + data)
    message = input(" -> ")

print('Received', repr(data))