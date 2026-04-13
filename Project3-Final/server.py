"""
Project 3 Server Python File

Names: Quentin Daniere, Luke Erlewein, Lucas Williams
"""

import socket
import threading

class Server:
    def __init__(self):
        self.host = "0.0.0.0"  # Listen on all interfaces so other machines can connect
        self.port = 5800
        self.connections = {}
        self.lock = threading.Lock()

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))

        local_ip = socket.gethostbyname(socket.gethostname())
        print(f"Connection IP: {local_ip}")
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

            msg = data.decode()
            cmd = msg.split()[1]

            match cmd:
                case "/list":
                    curr_users = ""
                    for id in list(self.connections.values()):
                        curr_users += f'{id}, '
                    curr_users = curr_users[:-2]
                    with self.lock:
                        socket.sendall(curr_users.encode())
                case "/w":
                    target_user = msg.split()[2]
                    new_msg = msg.split()
                    del new_msg[1:3]
                    new_msg = " ".join(new_msg)

                    target_socket = next((k for k, v in self.connections.items() if v == target_user), None)
                    with self.lock:
                        target_socket.sendall(new_msg.encode())

                case _:
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