# server for agar.io 
# Author : Loïc Pottier
# Creation date : 25/01/2022

# IMPORTS
import socket
import _thread
import sys
import pickle

# FILE IMPORTS
from game import Game

# NETWORK SECTION
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
    global game
    conn.send(pickle.dumps(game.players))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            direction = (data[0], data[1])
            name = data[2]
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", data)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except :
            break

    print("Lost connection")
    conn.close()

if __name__ == "__main__":

    game = Game()

    while True:
        conn, addr = s.accept()
        print("connected to: ", addr)

        _thread.start_new_thread(threaded_client, (conn,))