import socket
import sys

name = 'robot'

template = "msg({},dispatch,cliconsole,{},{},1)"


host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

running = True
while running:
    cmd = input("cmd> ")
    message = ''
    if cmd in ['w', 'a', 's', 'd', 'h', 'x', 'z']:
    	message = template.format('cmd', name, f'cmd({cmd})')
    elif cmd == "close":
        running = False
    else:
    	message = template.format(cmd.split('(')[0], name, cmd)
    message = message + '\n'
    print(message)
    sock.sendall(message.encode())

sock.close()
