import socket
from threading import Thread

clients={}
addresses={}

Host='127.0.0.1'
Port=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,Port))

def accept_clients_connections():
    while True:
        client_con,client_address=s.accept()
        print(client_address,"Has connected")
        client_con.send("Welcome to the chat room!".encode("utf8"))
        addresses[client_con]=client_address
        Thread(target=handle_client,args=(client_con,client_address)).start()
        
def broadcast(mgs,prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+mgs)
               
        
def handle_client(conn,addr):
    name=conn.recv(1024).decode("utf8")
    welcome="Welcome " + name + " you can type #quit if you want to leave the chat room"
    conn.send(bytes(welcome,"utf8"))
    
    mgs= name + " has recently joined the chat room"
    broadcast(bytes(mgs,"utf8"))
    clients[conn]=name
    while True:
        mgs=conn.recv(1024)
        
        if mgs!=bytes("#quit","utf8"):
            broadcast(mgs,name+" :")
        
        else:
            conn.send(bytes("#quit","utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name+ " has left the chat room","utf8"))
            
                        
                
            



if __name__=="__main__":
    s.listen(5)
    print("The server has been started and is now listening to clients requests")
    t1=Thread(target=accept_clients_connections)
    t1.start()
    t1.join()