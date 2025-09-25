import socket
import sys
from smart_tv import SmartTV
from handler import handle_command

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_socket(sock, host, port):
    sock.bind((host, port))

def listen_for_connection(sock):
    sock.listen()
    print(f"Server listening on {sock.getsockname()}")

def accept_connection(sock):
    return sock.accept()

def receive_command(conn):
    try:
        data = conn.recv(1024)
        if not data:
            return None
        return data.decode().strip()
    except:
        return "Error during communication!"
    
def close_socket(sock):
    sock.close()
    print("Server closed")

def main():
    host = "127.0.0.1"
    port = 1238

    smartTV = SmartTV()

    if len(sys.argv) > 1:
        try:
            port = sys.argv[1]
        except ValueError:
            print("Invalid port number. Using default 1238")

    server_socket = create_socket()

    try:
        bind_socket(server_socket, host, port)
        listen_for_connection(server_socket)

        conn, addr = accept_connection(server_socket)
        print(f"Server connected with {addr}")

        while True:
            command = receive_command(conn)

            if not command or command.lower() == "quit":
                conn.sendall(b"Goodbye!\n")
                break

            response = handle_command(smartTV, command)
            conn.sendall((response).encode())
            
    except:
        print("Server error")
    finally:
        close_socket(server_socket)

if __name__ == "__main__":
    main()
    