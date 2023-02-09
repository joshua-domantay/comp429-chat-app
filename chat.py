# Joshua Domantay, Ayush Thapaliya
# Professor Senhua Yu
# COMP 429 - 16938
# 4 March 2023

import sys
import _thread
from socket import *

port = 0
connections = []

def help():
    print("myip - Display IP address")
    print("myport - Display program port number")
    print("connect <destination> <port> - Connect to another peer")
    print("list - List every connected peer's IP address and port number")
    print("terminate - Close a connection")
    print("send <connection id> <message> - Send message to a peer")
    print("exit - Exit the program")

def myip():
    hostname = gethostname()
    return gethostbyname(hostname)      # Return ip address

def myport():
    return port

def connect(dest, port):
    pass

def list_connections():
    pass

def terminate(conn_id):
    pass

def send(conn_id, msg):
    pass

def setup_server(port):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((myip(), port))
    server_socket.listen(1)
    while True:
        conn_socket, addr = server_socket.accept()
        msg = conn_socket.recv(1024).decode()
        print("Message received from", addr[0])
        print("Sender's Port:", addr[1])
        print("Message:", msg)
        conn_socket.close()

def get_input():
    while True:
        x = input(">> ")
        x = x.split()
        if(x[0].lower() == "help"):
            help()
        elif(x[0].lower() == "myip"):
            print("The IP address is", myip())
        elif(x[0].lower() == "myport"):
            print("The program runs on port number", myport())
        elif(x[0].lower() == "connect"):
            # TODO connect()
            pass
        elif(x[0].lower() == "list"):
            # TODO list_connections()
            pass
        elif(x[0].lower() == "terminate"):
            # TODO terminate()
            pass
        elif(x[0].lower() == "send"):
            # TODO send()
            pass
        elif(x[0].lower() == "exit"):
            break
        else:
            pass    # Disregard

def main():
    # Get command line arguments
    arg_len = len(sys.argv)

    # If arguments contain port number...
    if((arg_len == 2) and (sys.argv[1].isdecimal())):
        port = int(sys.argv[1])
        try:    # If connection goes through...
            _thread.start_new_thread(setup_server, (port,))     # Thread for listening
            get_input()
        except:     # Else error message for no connection
            print("Connection error")
            return
    else:   # Else error message for lack of port number
        print("Please provide a port number on your arguments")

if __name__ == "__main__":
    sys.exit(main())
