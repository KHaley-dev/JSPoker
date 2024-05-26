import socket
import os
from dotenv import load_dotenv
import logger

load_dotenv()
main_logger = logger.Logger("test_client")

HEADER = int(os.environ.get("HEADER", 64))
PORT = int(os.environ.get("PORT", 5050))
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
main_logger.info(f"Connected to {ADDR}")
 

def send(message):
    message = message.encode(FORMAT)
    message_len = len(message)
    send_length = str(message_len).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    
    client.send(send_length)
    client.send(message)
    
def disconnect():
    send("ws/disconnect")
    
send("Hello world!")
disconnect()