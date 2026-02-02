"""
Project 2 Client Python File

Names: Quentin Daniere, Luke Erlewein, Lucas Williams
"""

import socket
import threading

class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5800

        self.listen_for_messages()
    
    def listen_for_messages(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))

            # listen for messages
            print("Waiting for a message")
            server.listen()
            
            connection, address = server.accept()
            print(f"Message from: {address}")

            with connection:
                while True:
                    data = connection.recv(2048)

                    if not data or data == bytes():
                        break
                    print(f'Received: {data.decode()}')
                
                    # Send back a message
                    message = input("Please reply with a return message: ")
                    connection.sendall(str(message).encode())

if __name__ == "__main__":
    server = Server()