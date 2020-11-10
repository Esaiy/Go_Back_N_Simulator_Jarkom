import socket
import time
from random import random

HOST = '127.0.0.1'  #IP
PORT = 65432        #port
l = []              #queue ack
n = 3               #window size
random_prob = 0.5   #loss probability


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            time.sleep(1)
            if not data:
                break
            data = data.decode('utf-8')
            if data[0] != '-':
                print('Frame {} received'.format(data))
                l.append(data)
            if len(l) >= n or data[0] == '-':
                if len(l) == 0:
                    conn.sendall('*'.encode('utf-8'))
                elif random() < random_prob:
                    time.sleep(2)
                    conn.sendall('Loss {}'.format(l.pop(0)).encode('utf-8'))
                    l.clear()
                else:
                    conn.sendall('Ack {}'.format(l.pop(0)).encode('utf-8'))
            else:
                conn.sendall('-'.encode('utf-8'))
