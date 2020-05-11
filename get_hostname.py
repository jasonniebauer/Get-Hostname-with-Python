#! /usr/bin/env python 

import socket


hostname = socket.gethostname()
print(hostname)

print(socket.gethostbyaddr('192.168.1.160'))

print(socket.getfqdn())  # Fully Qualified Domain Name

print(socket.gethostbyname('www.google.com'))

print(socket.gethostbyname_ex(hostname))

# for i in range(0, 20000):
#     try:
#         print('Port %s: %s' % (i, socket.getservbyport(i)))
#     except:
#         pass


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()