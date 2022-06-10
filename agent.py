# agent program to communicate with the server for get and send data to server by json and socket

# import libraries
import socket
import json
import time
import random
import psutil


class Agent:
    def __init__(self, HOST="127.0.0.1", PORT=8001):
        self.HOST = HOST
        self.PORT = PORT
        self.S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.S.connect((self.HOST, self.PORT))
    
    def get_sys_data(self):
        data = {
            "cpu_percent": psutil.cpu_percent(),
            "mem_percent": psutil.virtual_memory().percent
        }
        print(data)
        return data

    def send(self):
        self.S.send(json.dumps(self.get_sys_data()).encode('ascii'))
        print("Sent")


agent = Agent()

until_connected = False
while not until_connected:
    try:
        agent.connect()
        until_connected = True
        print("Connected to the server!")
    except ConnectionRefusedError:
        print("Can not connect to the server!")
        yes = input("Do you want to try again? [y/n]: ")
        if yes != "y":
            print("Agent program closed!")
            quit()

try:
    while True:
        try:
            agent.send()
        except :
            print("Can not send data to the server!")
        time.sleep(1)
except:
    print("Problem in sending data!")