import socket

from flask import render_template

PORT_BROADCAST_TO_CLIENTS = 37020
PORT_LISTEN_FOR_CLIENTS = 37021


def clients():
    friend_addrs = _send_clients_finder_broadcast()
    return render_template('clients.html', friends=friend_addrs)


def _send_clients_finder_broadcast():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    skt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.
    skt.settimeout(0.5)
    skt.bind(("", PORT_LISTEN_FOR_CLIENTS))
    message = b"just nod if you can hear me"
    skt.sendto(message, ('<broadcast>', PORT_BROADCAST_TO_CLIENTS))
    data, addr = skt.recvfrom(1024)
    return [data, addr]
