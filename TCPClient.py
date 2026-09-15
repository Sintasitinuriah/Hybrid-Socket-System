import socket

def start_tcp_client():
    serverName = '127.0.0.1'
    serverPort = 12000

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print("[CONNECTED] Terhubung ke TCP Server.")

    try:
        for i in range(3):
            pesan = f"Ini adalah pesan ke-{i+1}"
            # Menambahkan delimiter '\n' untuk menjaga batas pesan
            pesan_dengan_batas = pesan + '\n'
            clientSocket.send(pesan_dengan_batas.encode('utf-8'))
            
            # Menerima balasan dari server
            balasan = clientSocket.recv(1024).decode('utf-8')
            # Membersihkan delimiter \n saat ditampilkan
            print(f"Balasan Server: {balasan.strip()}")
    finally:
        clientSocket.close()

if __name__ == "__main__":
    start_tcp_client()