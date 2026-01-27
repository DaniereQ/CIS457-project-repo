"""
Project 1 Client Python File

Names: Quentin Daniere, Luke Erlewein, Lucas
"""

import socket

class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5800

        self.listen_for_messages()
    
    def listen_for_messages(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))

            # listen for messages
            server.listen()
            
            connection, addresss = server.accept()
            with connection:
                while True:
                    data = connection.recv(2048)
                    if not data:
                        break
                
                print(f'Received: {data.decode()}')

if __name__ == "__main__":
    server = Server()