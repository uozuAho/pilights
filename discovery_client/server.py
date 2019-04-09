import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
skt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
skt.bind(("", 37020))
while True:
    data, addr = skt.recvfrom(1024)
    print("received message: %s"%data)
    if data == "just nod if you can hear me":
        skt.sendto('nod', ('<broadcast>', 37021))
