import socket as sk
import random

HOST = "192.168.1.7"
PORT = 12348
server_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Server is running on {HOST}:{PORT}")

Packet_count = 10
Loss_Prob = 0.01

while True:
    req_packet, client_address = server_socket.recvfrom(1024)
    requested_packet = int(req_packet.decode())
    print(f"Received packet number {requested_packet} from {client_address}")

    if requested_packet < Packet_count:
        if random.random() > Loss_Prob:
            response = f"sending packet no {requested_packet}"
        else:
            response = "high loss probability"
    else:
        response = "unexpected packet number"
    
    server_socket.sendto(response.encode(), client_address)
    print(response)

server_socket.close()
