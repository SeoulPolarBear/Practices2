from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))#server( 내pc)의 ip , 내가 지정한 port 번호
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')


# from socket import*

# serverSock = socket(AF_INET, SOCK_STREAM)
# serverSock.bind((" ",8080))#" "는 0.0.0.0이란 뜻 ip 주소와 port 번호를 연동
# serverSock.listen(1)# 세션 개수 listen은 server 측에서 client를 받을 수 있게 준비하고 있는 단계이다.

# connectionSock, addr = serverSock.accept()#접속 했는지를 확인하는 부분

# print(str(addr),'에 접속이 확인되었습니다.')


# #print(socket.getservbyname("http","tcp"))# 각 app("http", "ftp"의 port 번호 출력 
# #print(socket.getservbyname("ftp","tcp"))

# s = socket.socket()#모듈.함수()



## client 부분 는 connect를 사용한다.

# ClientSock = socket(AF_INET, SOCK_STREAM)
# ClientSock.connect(('127.0.0.1',8080))#server쪽 port 번호를 사용해야 한다. # server에 접속하기 위해 server에 접속할 client 객체를 생성해준다.
# client의 port 번호는 연결 되는 순간 OS에서 49152~ 65535 사이의 port번호를 direct로 생성된다.
#(loop back interface) 내부에서 자기 자신에게 돌아오게 하는 test 용이다.

# print('연결 확인 됐습니다.')
# clientSock.send('I am a client'.encode('utf-8')) # 서버로 전달하는 data

# print('메시지를 전송했습니다.')

# data = clientSock.recv(1024) #서버에서 받은 data
# print('받은 데이터 : ', data.decode('utf-8'))

