import socket
import time

ACTOR_NAME = "robotmind"
PORT = 8020

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

goForwardMsg  = "msg(cmd,dispatch,python," + ACTOR_NAME + ",cmd(w),-1)"
goBackwardMsg = "msg(cmd,dispatch,python," + ACTOR_NAME + ",cmd(s),-1)" 
turnLeftMsg   = "msg(cmd,dispatch,python," + ACTOR_NAME + ",cmd(a),-1)"  
turnRightMsg  = "msg(cmd,dispatch,python," + ACTOR_NAME + ",cmd(d),-1)"  
haltMsg       = "msg(cmd,dispatch,python," + ACTOR_NAME + ",cmd(h),-1)"
stepMsg       = "msg(step,dispatch,python," + ACTOR_NAME + ",step({}),-1)"
stopMsg       = "msg(stop,dispatch,python," + ACTOR_NAME + ",stop(X),-1)"
loopMsg       = "msg(loop,dispatch,python," + ACTOR_NAME + ",loop(X),-1)"

def connect(port) :
    server_address = ('localhost', port)
    sock.connect(server_address)
    print("CONNECTED WITH basicrobot" , server_address)

def sendDispatch(message):
    print("sending ", message)
    msg = message + "\n"
    byt=msg.encode()
    sock.send(byt)

def work() :
    # sendDispatch(loopMsg)
    sendDispatch(stepMsg.format(10000))

def read() :
    BUFFER_SIZE = 1024
    data = sock.recv(BUFFER_SIZE)
    print( "received data:", data )

def terminate():
    sock.close()
    print("BYE")

###########################################    
connect(PORT)
work()
terminate()
