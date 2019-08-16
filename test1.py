import socket
addrs = socket.getaddrinfo(socket.gethostname(),None)
print('ipv4' + [item[4][0] for item in addrs if ':' not in item[4][0]][0])
