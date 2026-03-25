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

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

        print('Listening at', self.server.getsockname())

        self.listen_thread = threading.Thread(target=self.server_listen)

        self.listen_thread.start()
    
    def server_listen(self):
        self.server.listen()
        
        connection, name = self.server.accept()
        self.connections.append(connection)

        #Create a new thread here to listen to that connection
        socket_thread = threading.Thread(target=self.server_socket, args=(connection))
        socket_thread.start()
        
    def server_socket(self, socket):
            while True:
                data = socket.recv(2048)

                if not data or data == bytes():
                    break
                parts = str(data.decode).split(":")
                for conn in self.connections:
                    if conn != socket:
                        self.send_message(conn, parts[0], parts[1])

    def send_message(self, conn, user, msg):
            full_msg = f"{user}: {msg}"
            conn.sendall(full_msg.encode())
    
    def __del__(self):
        self.listen_thread.join()
        self.socket_thread.join()

if __name__ == "__main__":
    server = Server()