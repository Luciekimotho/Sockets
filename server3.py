import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #ipv4 & connection oriented tcp
except socket.error, msg:
	print ('Failed to  create socket. Error code: '+str(msg[0])+ 'Error message: ' +msg[1])
	sys.exit();
print ('Socket created')
