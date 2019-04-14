import socket

PORT_LISTEN = 37020
PORT_SEND = 37021


def main():
    my_ip = get_my_ip()

    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    skt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    skt.bind(("", PORT_LISTEN))

    print('listening for messages on port ' + str(PORT_LISTEN))

    while True:
        data, addr = skt.recvfrom(1024)
        print("received message: %s"%data)
        if data == "just nod if you can hear me":
            # todo: don't broadcast - send back to sender
            skt.sendto(my_ip, ('<broadcast>', PORT_SEND))


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()
    return my_ip


if __name__ == "__main__":
    main()
