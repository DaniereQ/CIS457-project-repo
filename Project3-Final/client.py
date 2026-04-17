"""
Project 3 Client Python File

Names: Quentin Daniere, Luke Erlewein, Lucas Williams
"""

import socket
import threading

class Client:
    def __init__(self):
        self.host = input("Enter server IP address: ")
        self.port = 5800
        self.running = True
        self.name = input("Enter client name: ")

        # Create socket and connect to host,port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.sendall(self.name.encode())

        self.send_thread = threading.Thread(target=self.send_message)
        self.receive_thread = threading.Thread(target=self.receive_message)

        self.send_thread.start()
        self.receive_thread.start()

        self.receive_thread.join()
        self.send_thread.join()

    def send_message(self):
        while self.running:
            msg = input()
            # Send a message
            if msg.lower() == "exit":
                self.running = False
                self.client.shutdown(socket.SHUT_RDWR)
                self.client.close()
                continue
            full_msg = f"{self.name}: {msg}"
            self.client.sendall(full_msg.encode())
        
    def receive_message(self):
        while self.running:
            try:
                data = self.client.recv(2048)
                if not data:
                    break
                print(f"{data.decode()}")
            except OSError:
                break
    
    def __del__(self):
        self.receive_thread.join()
        self.send_thread.join()


if __name__ == "__main__":
    client = Client()