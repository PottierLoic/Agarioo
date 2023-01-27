# network class for agar.io 
# Author : Loïc Pottier
# Creation date : 25/01/2022

# IMPORTS
import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.10"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.load(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.load(self.client.recv(2048))
        except socket.error as e:
            print(e)