import socket

PORT_LISTEN = 37020
PORT_SEND = 37021

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
skt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
skt.bind(("", PORT_LISTEN))

print('listening for messages on port ' + str(PORT_LISTEN))

while True:
    data, addr = skt.recvfrom(1024)
    print("received message: %s"%data)
    if data == "just nod if you can hear me":
        # todo: don't broadcast - send back to sender
        skt.sendto('nod', ('<broadcast>', PORT_SEND))
