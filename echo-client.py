#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))  # Connect to the server
  message = input(" -> ")  # Take user input
  # Allow user to send messages indefinitely (or until there is no connection to the server)
  while True:
    s.send(message.encode())
    data = s.recv(1024).decode()
    print(f'Received from server: {data}')  # Display back the message we sent to the server
    message = input(" -> ")  # Allow user to continue sending messages
