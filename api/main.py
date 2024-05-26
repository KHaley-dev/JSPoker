import socket
import threading
import os
from dotenv import load_dotenv
import logger

load_dotenv()
logger.set_level(logger.LogLevels.DEBUG)
main_logger = logger.Logger("main")

PORT = os.environ.get("PORT", 5050)
SERVER = os.environ.get("SERVER", socket.gethostbyname(socket.gethostname()))
ADDR = (SERVER, PORT)
main_logger.info(f"Binding server to {ADDR}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    pass

