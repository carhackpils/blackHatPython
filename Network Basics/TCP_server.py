import socket
import threading

bind_address = "0.0.0.0"
bind_port = 4568

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_address,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_address, bind_port)

def handle_client(client_socket):
    message = client_socket.recv(4096)
    print "[*] Received: %s" % message
    client_socket.send("ACK!")
    client_socket.close()
    
while True:
    client,addr = server.accept()
    print "[*] Accept connection from %s:%d" % (addr[0],addr[1])
    client_handler = threading.Thread(target=handle_client,args=(client))
    client_handler.start()
    
    
