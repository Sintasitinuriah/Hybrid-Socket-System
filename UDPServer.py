import socket
import random

def start_udp_server():
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    
    print(f"[STARTING] UDP Heartbeat Server berjalan di port {serverPort}...")

    while True:
        message, clientAddress = serverSocket.recvfrom(1024)
        
        # Simulasi packet loss (30% paket akan "hilang")
        if random.randint(1, 10) <= 3:
            print(f"[SIMULATED LOSS] Paket dari {clientAddress} diabaikan.")
            continue
        
        pesan_diterima = message.decode('utf-8')
        print(f"[PING MASUK] Menerima '{pesan_diterima}' dari {clientAddress}")
        
        # Mengirimkan balasan kembali ke klien
        balasan = f"PONG {pesan_diterima.split()[1]}"
        serverSocket.sendto(balasan.encode('utf-8'), clientAddress)

if __name__ == "__main__":
    start_udp_server()