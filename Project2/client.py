"""
Project 2 Client Python File

Names: Quentin Daniere, Luke Erlewein, Lucas Williams
"""

import socket
import threading

class Client:
    def __init__(self):
        self.host = socket.gethostname() # this is getting ur own address to send a message to yourself
        self.port = 5800
        # Create socket and connect to host,port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

        self.send_thread = threading.Thread(target=self.send_message)
        self.receive_thread = threading.Thread(target=self.receive_message)

        self.send_thread.start()
        self.receive_thread.start()

    def send_message(self):
        while True:
            msg = input()
            # Send a message
            self.client.sendall(msg.encode())
        
    def receive_message(self):
        while True:
            data = self.client.recv(2048)
            if not data:
                break
            print(f"Received: {data.decode()}")
    
    def __del__(self):
        self.receive_thread.join()
        self.send_thread.join()


if __name__ == "__main__":
    client = Client()