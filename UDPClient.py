import socket
import time

def start_udp_client():
    serverName = '127.0.0.1'
    serverPort = 12000

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Menetapkan batas timeout 1 detik sesuai spesifikasi tugas
    clientSocket.settimeout(1.0)
    
    rtt_list = []

    for sequence_number in range(1, 11):
        send_time = time.time()
        pesan = f"PING {sequence_number} {send_time}"
        
        try:
            clientSocket.sendto(pesan.encode('utf-8'), (serverName, serverPort))
            
            # Menunggu balasan (maksimal 1 detik)
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            receive_time = time.time()
            
            # Menghitung RTT dalam milidetik
            rtt = (receive_time - send_time) * 1000
            rtt_list.append(rtt)
            
            print(f"Reply dari {serverAddress}: {modifiedMessage.decode('utf-8')} | RTT = {rtt:.2f} ms")
            
        except socket.timeout:
            # Menangani paket yang hilang / unreliable packet delivery
            print(f"Request {sequence_number} timed out")

    clientSocket.close()

    # (Opsional) Menampilkan statistik ringkas
    if rtt_list:
        print("\n--- UDP Ping Statistics ---")
        print(f"RTT Tercepat: {min(rtt_list):.2f} ms")
        print(f"RTT Terlama: {max(rtt_list):.2f} ms")
        print(f"RTT Rata-rata: {sum(rtt_list)/len(rtt_list):.2f} ms")
        print(f"Packet Loss: {((10 - len(rtt_list)) / 10) * 100:.0f}%")

if __name__ == "__main__":
    start_udp_client()