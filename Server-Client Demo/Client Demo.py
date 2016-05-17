import socket
import sys

try:
	rpisock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
	print("Failed to create socket")
	sys.exit()
try:
	host=socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("Failed to get host")
	sys.exit()

rpisock.connect(host,80)
message="GET / HTTP/1.1\r\n\r\n"

try:
	rpisock.sendall(message)
except socket.error:
	print("Failed to send message")
	sys.exit()
data=rpisock.recv(1000)
print(data)
rpisock.close()
	