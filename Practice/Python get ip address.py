import socket
hostname=socket.gethostname()
ipaddr=socket.gethostbyname(hostname)
print("The computer name is {} and the ip address is {}".format(hostname,ipaddr))