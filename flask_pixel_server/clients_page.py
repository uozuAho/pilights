import socket

from flask import render_template

PORT_BROADCAST_TO_CLIENTS = 37020
PORT_LISTEN_FOR_CLIENTS = 37021


def clients():
    friends = _find_friends()
    return render_template('clients.html', friends=friends)


def _find_friends():
    skt = _open_socket()
    _broadcast_friend_finder_message(skt)
    friends = _listen_for_friends(skt)
    return friends

def _open_socket():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    skt.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    skt.settimeout(0.5)
    skt.bind(("", PORT_LISTEN_FOR_CLIENTS))
    return skt

def _broadcast_friend_finder_message(skt):
    message = b"just nod if you can hear me"
    skt.sendto(message, ('<broadcast>', PORT_BROADCAST_TO_CLIENTS))

def _listen_for_friends(skt):
    data, addr = skt.recvfrom(1024)
    return [Friend(data, addr[0])]


class Friend:
    def __init__(self, name, ip_addr):
        self.name = name
        self.ip_addr = ip_addr