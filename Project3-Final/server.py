"""
Project 3 Client Python File

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
        self.server.bind((self.host, self.port))

        print('Listening at', self.server.getsockname())

        self.listen_thread = threading.Thread(target=self.server_listen)

        self.listen_thread.start()
    
    def server_listen(self):
        self.server.listen()
        
        self.connection, name = self.server.accept()

        with self.connection:
            self.connections.append(self.connection)
            while True:
                data = self.connection.recv(2048)

                if not data or data == bytes():
                    break
                parts = str(data.decode).split(":")
                for conn in self.connections:
                    if conn != self.connection:
                        self.send_message(parts[0], parts[1])

    def send_message(self, user, msg):
            
            full_msg = f"{user}: {msg}"
            self.connection.sendall(full_msg.encode())
    
    def __del__(self):
        self.listen_thread.join()
        self.send_thread.join()

if __name__ == "__main__":
    server = Server()