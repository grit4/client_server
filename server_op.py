import socket
host=socket.gethostname()
port=9999
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((host,port))
print("Listening")
soc.listen(5)
con,addr=soc.accept()
print(addr)
s=con.recv(4098)
s=s.decode()
print("Computing")
r=eval(s)
r=str(r)
con.sendall(r.encode())
con.close()
print("Disconnected")