import datetime
import hashlib

def generate_room_id():
    now = datetime.datetime.now()
    hash_object = hashlib.sha256(f"{now}:.5f".encode("utf-8"))
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    int_hex = int(hex_dig, 16)
    print(int_hex)
    return int_to_roomid(int_hex)

def int_to_roomid(room_int: int) -> str:
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    encoded = []

    while room_int > 0:
        room_int, remainder = divmod(room_int, base)
        encoded.append(characters[remainder])
    
    while len(encoded) < 8:
        encoded.append('0')
    
    return ''.join(reversed(encoded))[:8]

def test_room_generator():
    while True:
        input(">>>")
        print("    Generated RoomID:", generate_room_id())

if __name__ == "__main__":
    test_room_generator()


