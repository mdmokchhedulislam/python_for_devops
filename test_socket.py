import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = "127.0.0.1"
port = 1234

server_socket.bind((host, port))

server_socket.listen(1)

print(f'serveer listening address is {host} and port is {port}' )