import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
soc.connect((host,port))
print("Connected")
str=input("Enter expression : ")
soc.sendall(str.encode())
r=soc.recv(4098)
print("Result : ",r.decode())
print("Disconnected")
soc.close()