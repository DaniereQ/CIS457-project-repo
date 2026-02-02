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

    def send_message(self, msg: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            # Create socket and connect to host,port
            client.connect((self.host, self.port))

            # Send a message
            print(f'Sending: {msg}')
            client.sendall(msg.encode())
            
            # Receive the reply message back
            data = client.recv(2048)
            print(f"Reply from server: {data.decode()}")


if __name__ == "__main__":
    client = Client()
    message = input("Please enter a message: ")
    client.send_message(message)