#!/usr/bin/python3
"""
Simple client-server application for dictionary serialization over sockets.
"""
import socket
import json


def start_server():
    """
    Sets up a server to listen for a connection, receive serialized JSON data,
    and deserialize it.
    """
    host = 'localhost'
    port = 65432

    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Bind the socket to the address and port
            s.bind((host, port))
            s.listen()
            # print(f"Server listening on {host}:{port}...")

            conn, addr = s.accept()
            with conn:
                # Receive data from the client
                data = conn.recv(1024)
                if data:
                    # Deserialize JSON data back to dictionary
                    received_dict = json.loads(data.decode('utf-8'))
                    print("Received Dictionary from Client:")
                    print(received_dict)
    except Exception as e:
        print(f"Server error: {e}")


def send_data(dictionary):
    """
    Connects to the server, serializes a dictionary to JSON, and sends it.
    """
    host = 'localhost'
    port = 65432

    if not isinstance(dictionary, dict):
        return

    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            # Serialize dictionary to JSON string and then to bytes
            serialized_data = json.dumps(dictionary).encode('utf-8')
            s.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Error: Connection refused. Is the server running?")
    except Exception as e:
        print(f"Client error: {e}")
