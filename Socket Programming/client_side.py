import socket

s=socket.socket()
host='localhost'
port=8080

s.connect((host,port))  #bağlantı kur
fileName="deneme.txt"
s.send(fileName.encode())
readFile=s.recv(1024)
print(readFile.decode())
s.close()

# message=s.recv(1024)

# while message:
#     print("Message",message.decode)
#     message.recv(1024)
    
    