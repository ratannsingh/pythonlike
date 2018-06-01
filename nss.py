#!/use/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rec_ip="192.168.1.27"
myport=9375
s.bind((rec_ip,myport))
while 4>2 :
 print s.recvfrom(100)












9
