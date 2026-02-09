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
        self.connection = None

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        print('Listening at', self.server.getsockname())

        self.listen_thread = threading.Thread(target=self.server_listen)
        self.send_thread = threading.Thread(target=self.send_message)

        self.listen_thread.start()
        self.send_thread.start()
    
    def server_listen(self):

        while True:
            self.server.listen()
            
            self.connection, name = self.server.accept()

            with self.connection:
                while True:
                    data = self.connection.recv(2048)

                    if not data or data == bytes():
                        break
                    print(f'{name}: {data.decode()}')

    def send_message(self):
        while True:
            msg = input()
            # Send a message
            self.connection.sendall(msg.encode())
    
    def __del__(self):
        self.listen_thread.join()
        self.send_thread.join()

if __name__ == "__main__":
    server = Server()