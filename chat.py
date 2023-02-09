# Joshua Domantay, Ayush Thapaliya
# Professor Senhua Yu
# COMP 429 - 16938
# 4 March 2023

import sys
import _thread
from socket import *

port = 0
connections = []
curr_id = 1

def valid_port(port):
    if(port.isdecimal()):
        n = int(port)
        if((n >= 0) and (n <= 65535)):
            return True
    return False

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
    try:
        # TODO: Test if connection is valid
        # testSocket = socket(AF_INET, SOCK_STREAM)
        # testSocket.connect((dest, port))

        # If connection is successful
        global curr_id
        connections.append((curr_id, dest, port))
        curr_id = curr_id + 1
    except Exception as e:
        print("Connection error", e)

def list_connections():
    pass

def terminate(conn_id):
    pass

def send(conn_id, msg):
    for i in range(len(connections)):
        if(int(connections[i][0]) == conn_id):
            # Send a message
            client_socket = socket(AF_INET, SOCK_STREAM)
            client_socket.connect((connections[i][1], connections[i][2]))
            client_socket.send(msg.encode())
            client_socket.close()
            return
    print("Connection id not found")

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
            if(len(x) == 3):
                if(valid_port(x[2])):
                    connect(x[1], int(x[2]))
                else:
                    print("Invalid port number")
            else:
                print("Please provide the destination and the port number")
        elif(x[0].lower() == "list"):
            # TODO list_connections()
            pass
        elif(x[0].lower() == "terminate"):
            # TODO terminate()
            pass
        elif(x[0].lower() == "send"):
            if(len(x) >= 3):
                if(x[1].isdigit()):
                    msg = x[2:]
                    msg = ' '.join(msg)
                    send(int(x[1]), msg)
                else:
                    print("Invalid connection id")
            else:
                print("Please provide the connection id and the message")
        elif(x[0].lower() == "exit"):
            break
        else:
            print(connections)
            # pass    # Disregard

def main():
    # Get command line arguments
    arg_len = len(sys.argv)

    # If arguments contain port number...
    if((arg_len == 2) and (valid_port(sys.argv[1]))):
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
