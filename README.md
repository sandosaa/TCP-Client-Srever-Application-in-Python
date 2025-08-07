# TCP-Client-Srever-Application-in-Python
This project demonstrates a simple TCP client-server application in Python, now provided as a single CLI tool.

## Requirements

- Python 3.x (no external dependencies; uses only the standard library)

## Usage

The CLI app (`tcp_cli.py`) supports both server and client modes.

### Run as Server

```bash
python tcp_cli.py server --host 0.0.0.0 --port 9999
```

- `--host`: Host/IP to bind the server (default: 0.0.0.0)
- `--port`: Port to bind the server (default: 9999)

### Run as Client

```bash
python tcp_cli.py client --host <server_ip> --port 9999 --message "Hello, Server!"
```

- `--host`: Server host/IP to connect to (required)
- `--port`: Server port to connect to (required)
- `--message`: Message to send to the server (default: "Hello, Server!")

## Example

Start the server in one terminal:

```bash
python tcp_cli.py server --host 0.0.0.0 --port 9999
```

Run the client in another terminal:

```bash
python tcp_cli.py client --host 127.0.0.1 --port 9999 --message "Test message"
```

## Features

- Modular code with error handling
- Easily configurable via CLI arguments
- No external dependencies
