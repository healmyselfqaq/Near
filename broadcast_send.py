from socket import *
from time import sleep
#设定目标地址（广播地址）
dest=('176.17.1.255',8888)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while 1:
    sleep(2)
    s.sendto('学生小姐上门服务，加Ｖ'.encode(),dest)
s.close()    