#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author: Quadra-V speech studio
# date: 2021-11-16
# contact: coolephemeroptera@gmail.com / 605686962@qq.com


import socket
import sys

class CLIENT():
    def __init__(self,host,port):
        self.c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.c.connect((self.host,self.port))

    def run(self):
        word = sys.argv[1]
        self.c.send(word.encode('utf-8'))
        data = self.c.recv(1024)
        print(data.decode())
        self.c.close()


def main():
    # server address
    ip = "110.40.150.238"
    port = 2223

    s = CLIENT(ip,port)
    s.run()

if __name__ == "__main__":
    main()
