import socket  # noqa: F401
import time


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept() # wait for client

    connection, _ = server_socket.accept()
    connection.sendall(b"+PONG\r\n")

if __name__ == "__main__":
    main()
