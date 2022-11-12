from socket import *

def receive(Sock):
    recvData = Sock.recv(1024)
    print('상대방 :', recvData.decode('utf-8'))

def send(Sock):
    sendData = input('>>>')
    Sock.send(sendData.encode('utf-8'))

port = 8080
ClientSock = socket(AF_INET, SOCK_STREAM)
ClientSock.connect(('127.0.0.1', port))


print("접속 완료")
while True:
    receive(ClientSock)
    send(ClientSock)
    
    
    
# port = 8080
# ClientSock = socket(AF_INET, SOCK_STREAM)
# ClientSock.connect(('127.0.0.1', port))


# print("접속 완료")
# while True:
    
#     recvData = ClientSock.recv(1024)
#     print('상대방 :', recvData.decode('utf-8'))
    
#     sendData = input('>>>')
#     ClientSock.send(sendData.encode('utf-8'))
