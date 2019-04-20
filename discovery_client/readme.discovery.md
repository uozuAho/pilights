# How to find other pilights on the network - 'discovery'

## option 1: discovery udp client + server
- client broadcasts its presence periodically
- server listens for broadcasts and stores clients in a file/db

## option 2: discover page within pilights server
- on page load, send a broadcast to ask for all pilights to respond
- discovery servers running on other pilights respond, results show on page

better than option 1:
- no need for file/db maintenance
- no need for periodic broadcast