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
        # Check if connecting to self
        if((dest == myip()) and (port == myport())):
            print("Cannot connect to self")
            return

        # Check if already connected to dest and port
        for conn in connections:
            if((conn[1] == dest) and (conn[2] == port)):
                print("Connection already established")
                return

        # Check connection and let peer know
        test_socket = socket(AF_INET, SOCK_STREAM)
        test_socket.connect((dest, port))
        msg = "con " + str(myport())
        test_socket.send(msg.encode())
        test_socket.close()

        # If connection is successful, add info to connections
        global curr_id
        connections.append((curr_id, dest, port))
        curr_id = curr_id + 1
    except Exception as e:
        print("Connection error")

def list_connections():
    #Prints out the list of connection#
    print("id:".ljust(12) + "IP address".ljust(20) + "Port No.")
    for conn in connections:
        print(str(conn[0]).ljust(12) + str(conn[1]).ljust(20) + str(conn[2]))

def terminate(conn_id):
    ##Terminate the connection list based on curr_id##
    found = False

    for conn in connections:
        if conn[0] == conn_id:
            # Check connection and let peer know
            a_socket = socket(AF_INET, SOCK_STREAM)
            a_socket.connect((conn[1], conn[2]))
            msg = "end " + str(myport())
            a_socket.send(msg.encode())
            a_socket.close()

            connections.remove(conn)
            found = True
            print(f"Connection with id {conn_id} has been terminated")
            break
    if not found:
        print(f"No connection found with an id {conn_id}")

def send(conn_id, msg):
    for i in range(len(connections)):
        if(int(connections[i][0]) == conn_id):
            # Send a message
            try:
                client_socket = socket(AF_INET, SOCK_STREAM)
                client_socket.connect((connections[i][1], connections[i][2]))
                msg = "msg " + str(myport()) + " " + msg
                client_socket.send(msg.encode())
                client_socket.close()
            except Exception as e:
                print(e)
            return
    print("Connection id not found")

def exit_chat():
    while(len(connections) > 0):
        terminate(connections[0][0])    # Terminate first connection

# TODO: When peer connects, establish connection as well
# TODO: When peer terminates, remove peer from list
def setup_server(port):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((myip(), port))
    server_socket.listen(1)
    while True:
        conn_socket, addr = server_socket.accept()
        msg = conn_socket.recv(1024).decode()
        msg_info = msg[:20]
        msg_info = msg_info.split(" ")
        
        if(msg_info[0] == "msg"):       # When message is received
            real_msg = msg[(len(msg_info[0]) + 1 + len(msg_info[1]) + 1):]
            print("\nMessage received from", addr[0])
            print("Sender's Port:", msg_info[1])
            print("Message:", real_msg)
        elif(msg_info[0] == "con"):     # When other peer tries to connect
            print("\nThe following peer established a connection with you:")
            print(f"\t\tIP: {addr[0]}, Port: {msg_info[1]}")
        else:       # When peer uses terminate
            print(f"\nPeer {addr[0]} with port {msg_info[1]} has terminated their a connection with you")
        print("\n>> ", end="")

        conn_socket.close()

def get_input():
    while True:
        x = input(">> ")
        x = x.split(" ")
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
            list_connections()
        elif(x[0].lower() == "terminate"):
            if(len(x) == 2):
                if(x[1].isdigit()):
                    terminate(int(x[1]))
            else:
                print("Please provide connection id")
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
            exit_chat()
            break
        print()

def main():
    # Get command line arguments
    arg_len = len(sys.argv)

    # If arguments contain port number...
    if((arg_len == 2) and (valid_port(sys.argv[1]))):
        global port
        port = int(sys.argv[1])
        if(True):
            _thread.start_new_thread(setup_server, (port,))     # Thread for listening
            get_input()
    else:   # Else error message for lack of port number
        print("Please provide a port number on your arguments")

if __name__ == "__main__":
    sys.exit(main())
