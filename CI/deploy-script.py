import socket
from config import SETTINGS

print("Deploy script here")

settings = SETTINGS()

IPADDRESS = settings.IPADDRESS
PORT = settings.PORT

conn = socket.socket()
conn.connect( (IPADDRESS, PORT) )
print("Connected")
conn.send(bytes('build', encoding="utf8"))
conn.close()
print("Sent")
