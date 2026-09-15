import socket
import threading

def handle_client(connectionSocket, addr):
    print(f"[NEW CONNECTION] Klien {addr} terhubung.")
    try:
        buffer = ""
        while True:
            # Menerima data dalam aliran byte
            data = connectionSocket.recv(1024).decode('utf-8')
            if not data:
                break
            
            buffer += data
            # Menangani Message Boundary menggunakan delimiter '\n'
            while '\n' in buffer:
                pesan, buffer = buffer.split('\n', 1)
                print(f"[PESAN MASUK] dari {addr}: {pesan}")
                
                # Membalas pesan ke klien (tambahkan \n kembali sebagai batas)
                balasan = f"Server menerima: {pesan}\n"
                connectionSocket.send(balasan.encode('utf-8'))
    except ConnectionResetError:
        print(f"[ERROR] Koneksi terputus dari {addr}")
    finally:
        print(f"[DISCONNECTED] Klien {addr} ditutup.")
        connectionSocket.close()

def start_tcp_server():
    serverPort = 12000
    # Membuat welcoming socket TCP
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f"[STARTING] TCP Server berjalan di port {serverPort}...")

    while True:
        # Menerima koneksi baru
        connectionSocket, addr = serverSocket.accept()
        # Spawn thread baru untuk klien tersebut
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_tcp_server()