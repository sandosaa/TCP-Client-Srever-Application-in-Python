#!/usr/bin/env python3

import argparse
import socket
import sys

def run_server(host: str, port: int):
    """Run the TCP server."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port} ...")
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            try:
                message = client_socket.recv(1024).decode('utf-8')
                print(f"Received data: {message}")
                client_socket.send("Message received".encode('utf-8'))
            except Exception as e:
                print(f"Error during client communication: {e}")
            finally:
                client_socket.close()
                print(f"Connection with {client_address} closed.")
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        try:
            server_socket.close()
        except Exception:
            pass

def run_client(host: str, port: int, message: str):
    """Run the TCP client."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received response from server: {response}")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        try:
            client_socket.close()
        except Exception:
            pass

def main():
    parser = argparse.ArgumentParser(
        description="TCP Client-Server CLI Application"
    )
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Mode to run: server or client")

    # Server mode arguments
    server_parser = subparsers.add_parser("server", help="Run as TCP server")
    server_parser.add_argument("--host", default="0.0.0.0", help="Host/IP to bind the server (default: 0.0.0.0)")
    server_parser.add_argument("--port", type=int, default=9999, help="Port to bind the server (default: 9999)")

    # Client mode arguments
    client_parser = subparsers.add_parser("client", help="Run as TCP client")
    client_parser.add_argument("--host", required=True, help="Server host/IP to connect to")
    client_parser.add_argument("--port", type=int, required=True, help="Server port to connect to")
    client_parser.add_argument("--message", default="Hello, Server!", help="Message to send to the server (default: 'Hello, Server!')")

    args = parser.parse_args()

    if args.mode == "server":
        run_server(args.host, args.port)
    elif args.mode == "client":
        run_client(args.host, args.port, args.message)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
