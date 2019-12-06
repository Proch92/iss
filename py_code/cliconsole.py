import socket
import sys


cmd_template = "msg(cmd,dispatch,cliconsole,robot,cmd({}),1)"


host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    cmd = input("cmd> ")
    message = cmd_template.format(cmd) + '\n'
    print(message)
    sock.sendall(message.encode())
