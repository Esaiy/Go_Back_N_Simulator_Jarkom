import socket
import time

frame = [x+1 for x in range(int( input('Total frame : ')))]

HOST = '127.0.0.1'          #ip
PORT = 65432                #port
top = bot = total_sent = 0  #init 0
print_state = False         #state for printing
n = 3                       #window size


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        time.sleep(1)
        if print_state:
            print(data)
        
        if top < len(frame):
            print('Frame {} sent...'. format(frame[top]))
            s.sendall(str(frame[top]).encode('utf-8'))
            total_sent += 1
        else:
            s.sendall('-'.encode('utf-8'))
        if top-bot == n or top == len(frame):
            bot+=1
        top+=1
        data = s.recv(1024).decode('utf-8')

        if data[:4] == 'Loss':
            top = bot

        if data[0] == '*':
            break
        elif data[0] == '-':
            print_state = False
        else:
            print_state = True

print('\nTotal frame sent : {}'.format(total_sent))
