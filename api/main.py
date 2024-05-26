import socket
import threading
import os
from dotenv import load_dotenv
import logger

load_dotenv()
main_logger = logger.Logger("main")

HEADER = int(os.environ.get("HEADER", 64))
PORT = int(os.environ.get("PORT", 5050))
SERVER = os.environ.get("SERVER", socket.gethostbyname(socket.gethostname()))
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "ws/disconnect"

main_logger.debug(f"Binding server to {SERVER}:{PORT}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

handle = logger.Logger("main.handle_client")
PADDING = "\t" * 8
def handle_client(conn, addr):
    handle.info(f"Received new connection\n{PADDING}* Address: {addr} connected\n{PADDING}* Currently active connections: {threading.active_count() - 1}")
    
    connected = True
    while connected:
        message_len = conn.recv(HEADER).decode(FORMAT)
        if message_len: 
            message_len = int(message_len)
            
            message = conn.recv(message_len).decode(FORMAT)
            main_logger.info(f"Received message from {addr}\n{PADDING}* Message: {message}")
            if message == DISCONNECT_MESSAGE:
                connected = False
                main_logger.debug(f"Disconnecting client {addr}...")
            
    conn.close()
    main_logger.info(f"Client {addr} successfully disconnected")

def starter():
    here = logger.Logger("main.starter")
    server.listen()
    here.info("Server is listening")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()

main_logger.info("Starting server...")
starter()

