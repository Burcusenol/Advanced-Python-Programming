import socket

host='localhost'
port=8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #(family,type)->(tcp protocol,tcp bağlantı tipi )
s.bind((host,port))
s.listen(1) #one connection
print("The server is listening for client request on port",port)
conn,adress=s.accept() #connection success
print("Connection has been established from ",str(adress))

try:
    fileName=conn.recv((1024))  #1 sn max 1024 byte
    file=open(fileName,'rb')
    readFile=file.read()
    conn.send(readFile)
    file.close()
    conn.close() #conn close
except:
    conn.send("File Not Found on the server".encode())