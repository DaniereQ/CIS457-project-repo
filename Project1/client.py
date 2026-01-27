"""
Project 1 Client Python File

Names: Quentin Daniere, Luke Erlewein, Lucas
"""

import socket

class Client:
    def __init__(self):
        self.host = socket.gethostname() # this is getting ur own address to send a message to yourself
        self.port = 5800

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self, msg: str):
        try:
            self.client_socket.connect(self.host, self.port)
        except:
            print("The connection failed")
            return
        
        print(f'Sending: {msg}')
        self.client_socket.sendall(msg.encode())
        self.client_socket.close()


if __name__ == "__main__":
    client = Client()
    client.send_message("Hello World!")