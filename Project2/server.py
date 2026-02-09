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
        self.connections = []

        self.run()
    
    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        print('Listening at', server.getsockname())

        while True:
            server.listen()
            
            connection, name = server.accept()

            with connection:
                while True:
                    data = connection.recv(2048)

                    if not data or data == bytes():
                        break
                    print(f'Received: {data.decode()}')

    
if __name__ == "__main__":
    server = Server()