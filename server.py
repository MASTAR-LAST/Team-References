import socket as sc
import threading as th
import getpass
import timeit
import time

PORT = 5050
FORMAT = "utf-8"
BAN = ["fuck", "bitch"]
DES = 'DES'
BAN_IP = []
HEADER = 64
SERVER = sc.gethostbyname(sc.gethostname())
ADDR = (SERVER, PORT)

server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind(ADDR)

def send():
    ...
def client(conn, addr, username):
    if addr in BAN_IP:
        print("YOU HAVE BEEN BANED")
        conn.close()

    print("New Client Have Been Joined!")
    print(f"ip: {addr}")

    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f"{username}: {msg}")

            for msg_ in msg:
                if msg_.lower() in BAN:
                    BAN_IP.append(addr)
                    print(f"YOU HAVE BEEN BAN FORM SERVER FOR TYPE {msg_}")
                    connected = False

            if msg.lower() == DES.lower():
                connected = False

    conn.close()


def start():
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    server.listen()
    print(f"Start Listing to {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = th.Thread(target=client, args=(conn, addr, username))
        thread.start()

print("Starting server...")
start()