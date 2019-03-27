#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # IPv4 equivalent of localhost
PORT = 65432        # Arbitrary non-privileged port

# socket.socket() creates a new socket object, which takes in an address family
# and socket type. AF_INET is the Internet address family for IPv4 SOCK_STREAM
# specifies that the socket type will be TCP, the protocol we'll be using to
# transfer messages in the network.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  # Allow the server to accept connections (can also optionally supply the backlog value)
  s.listen()
  # accept() blocks & waits for incoming connections. Once done, it returns a new
  # socket object representing the connection and a tuple representing the client's
  # address (host, port) in this case (different for IPv6).
  conn, addr = s.accept()

  print('Connected by', addr)  # Confirm connection from client to server
  while True:  # Socket listens indefinitely (but can be terminated with Ctrl-c)
    data = conn.recv(1024).decode()
    if data:
      print(data)  # Allows us to see what messages were sent to the server
      with open("log.txt", 'a') as f:
        f.write(data + '\n')  # Log received messages to a separate file

      conn.sendall(data.encode())  # Sends the message back to the client (like a receipt)
