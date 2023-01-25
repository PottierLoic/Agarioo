# network class for agar.io 
# Author : Loïc Pottier
# Creation date : 25/01/2022

# IMPORTS
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.10"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.data = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def senf(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)