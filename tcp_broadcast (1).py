import socket
import threading
import sys

HOST = socket.gethostname(socket.gethostbyname())
PORT = 12345

clients = []

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message)
            except Exception:
                clients.remove(client)
                client.close()

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    clients.append(client_socket)
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[{address}] {data.decode('utf-8')}")
            broadcast(data, sender_socket=client_socket)
    except Exception as e:
        print(f"[!] Exception with {address}: {e}")
    finally:
        print(f"[-] Connection closed: {address}")
        clients.remove(client_socket)
        client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    try:
        while True:
            client_socket, address = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, address), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter server IP (default 127.0.0.1): ") or "127.0.0.1"
    try:
        client_socket.connect((server_ip, PORT))
        print(f"Connected to server at {server_ip}:{PORT}")

        def listen():
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"\n[Broadcast] {data.decode('utf-8')}")
                except Exception:
                    break

        threading.Thread(target=listen, daemon=True).start()

        while True:
            msg = input()
            if msg.lower() in ("exit", "quit"):
                break
            client_socket.sendall(msg.encode('utf-8'))
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    mode = input("Run as (server/client): ").strip().lower()
    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("Invalid mode. Use 'server' or 'client'.")
