##############################################################
# basicrobotusage.py
# sendDispatch       : sends a command in output
# read               : acquires data from input
##############################################################
import socket
import time

mindPort = 8023
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

goForwardMsg  = "msg(cmd,dispatch,python,robotmind,cmd(w),-1)"
goBackwardMsg = "msg(cmd,dispatch,python,robotmind,cmd(s),-1)" 
turnLeftMsg   = "msg(cmd,dispatch,python,robotmind,cmd(a),1)"  
turnRightMsg  = "msg(cmd,dispatch,python,robotmind,cmd(d),1)"  
haltMsg       = "msg(cmd,dispatch,python,robotmind,cmd(h),1)"
stepMsg       = "msg(step,dispatch,python,robotmind,step({}),-1)"
stopMsg       = "msg(stop,dispatch,python,robotmind,stop(X),-1)"

def connect(port) :
    server_address = ('localhost', port)
    sock.connect(server_address)    
    print("CONNECTED WITH basicrobot" , server_address)

def sendDispatch( message ) :
    print("sending ", message)
    msg = message + "\n"
    byt=msg.encode()
    sock.send(byt)

def work() :
    sendDispatch( stepMsg.format(2000) )
    time.sleep(1)
    sendDispatch( stopMsg )

def read() :
    BUFFER_SIZE = 1024
    data = sock.recv(BUFFER_SIZE)
    print( "received data:", data )

def terminate() :
    sock.close()
    print("BYE")

###########################################    
connect(mindPort)
work()
terminate()  
