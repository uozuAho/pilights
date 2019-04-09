""" Use this to test the server """

import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
client.settimeout(0.2)
client.bind(("", 44444))
message = b"just nod if you can hear me"
while True:
    client.sendto(message, ('<broadcast>', 37020))
    print("message sent!")
    time.sleep(1)