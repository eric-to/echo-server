#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()

  print('Connected by', addr)
  while True:
    data = conn.recv(1024).decode()
    if data:
      print(data)

      with open("log.txt", 'a') as f:
        f.write(data + '\n')

      conn.sendall(data.encode())
