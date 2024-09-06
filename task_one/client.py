import socket as sk

ip = "192.168.1.7"
port = 12348

client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

expected_packet = 0
Packet_count = 10

while expected_packet < Packet_count:
    try:
       
        packet_data = str(expected_packet).encode()
        client_socket.sendto(packet_data, (ip, port))
        print(f"Requesting packet: {expected_packet}")

        
        response, _ = client_socket.recvfrom(1024)
        response = response.decode()

        if response == f"sending packet no {expected_packet}":
            expected_packet += 1
        elif response == "unexpected packet number":
            print("Unexpected packet number")
        else:
            print("Received an unexpected response")

    except Exception as e:
        print(f"An error occurred: {e}")

client_socket.close()
