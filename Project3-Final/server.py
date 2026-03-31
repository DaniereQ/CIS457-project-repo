"""
Project 3 Server Python File

Names: Quentin Daniere, Luke Erlewein, Lucas Williams
"""

import socket
import threading

class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5800
        self.connections = {}
        self.lock = threading.Lock()

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))

        print('Listening at', self.server.getsockname())

        self.listen_thread = threading.Thread(target=self.server_listen)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def server_listen(self):
        self.server.listen()

        while True:
            connection, address = self.server.accept()
            name = connection.recv(2048).decode()
            print(f"{name} connected from {address}")

            with self.lock:
                self.connections[connection] = name

            socket_thread = threading.Thread(target=self.server_socket, args=(connection, name))
            socket_thread.daemon = True
            socket_thread.start()

    def server_socket(self, socket, name):
        while True:
            data = socket.recv(2048)

            if not data:
                with self.lock:
                    del self.connections[socket]
                print(f"{name} disconnected")
                break

            # Parse message here

            with self.lock:
                for conn in self.connections:
                    if conn is not socket:
                        conn.sendall(data)

if __name__ == "__main__":
    server = Server()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nClosing Server")