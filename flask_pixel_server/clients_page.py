import socket

from flask import render_template


def clients():
    _send_clients_finder_broadcast()
    return render_template('clients.html', name='yoyoyo')


def _send_clients_finder_broadcast():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    skt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.
    skt.settimeout(0.2)
    skt.bind(("", 37021))
    message = b"just nod if you can hear me"
    skt.sendto(message, ('<broadcast>', 37020))
    data, addr = skt.recvfrom(1024)
    print("received message: %s"%data)