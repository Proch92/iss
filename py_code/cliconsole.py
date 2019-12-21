import socket
import sys

name = 'robotmind'

template = "msg({},dispatch,cliconsole,{},{},1)"


host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    cmd = input("cmd> ")
    message = ''
    if cmd in ['w', 'a', 's', 'd', 'h']:
    	message = template.format('cmd', name, f'cmd({cmd})')
    else:
    	message = template.format(cmd.split('(')[0], name, cmd)
    message = message + '\n'
    print(message)
    sock.sendall(message.encode())
