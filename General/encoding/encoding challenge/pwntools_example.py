import base64
from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    if received["type"] == "base64":
        decoded = base64.b64decode(received["encoded"]).decode()
    elif received["type"] == "hex":
        decoded = bytes.fromhex(received["encoded"]).decode()
    elif received["type"] == "rot13":
        decoded = codecs.decode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        decoded = long_to_bytes(int(received["encoded"], 16)).decode()
    elif received["type"] == "utf-8":
        decoded = ''.join([chr(i) for i in received["encoded"]])
    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

    # json_recv()
