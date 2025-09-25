import socket

def create_client_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server(sock, host, port):
    sock.connect((host, port))
    print("Connected to server")

def receive_data(sock):
    return sock.recv(1024)

def read_send_command(sock):
    while True:
        command = input("IDATA2304>>")
        sock.sendall((command).encode())
        response = sock.recv(1024).decode().strip()
        print(response)
        
        if command.lower() == "quit":
            break

def main():
    host = "127.0.0.1"
    port = 1238
    sock = create_client_socket()

    try:
        connect_to_server(sock, host, port)
        response = receive_data(sock)

        print(response.decode(errors='ignore'))
        read_send_command(sock)
    except:
        print("An error occured")
    finally:
        sock.close()

if __name__ == "__main__":
    main()