# server for agar.io 
# Author : Loïc Pottier
# Creation date : 25/01/2022

# IMPORTS
import socket
import _thread
import sys

server = "192.168.0.10"
port = 5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)

print("waiting for a connection, server started")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except :
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("connected to: ", addr)

    _thread.start_new_thread(threaded_client, (conn,))