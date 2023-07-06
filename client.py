import socket as sc
import threading as th

PORT = 5050
FORMAT = 'utf-8'
DES = 'DES'
HEADER = 64
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    MSG = msg.encode(FORMAT)
    msg_len = len(MSG)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b''*(HEADER - len(send_len))
    client.send(send_len)
    client.send(MSG)

while True:

    massage = input("Enter your massage: ")
    send(massage)
