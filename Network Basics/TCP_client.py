import socket

target_port = 4567
target_host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("HELLO")

response = client.recv(4096)

print response