# Simple Chat App with Python
Programmed by Joshua Anthony Domantay and Ayush Thapaliya.

## Contribution made by Joshua Anthony Domantay
1. Check if a port number is valid.
2. Connect with a peer using their IP address and listening port number.
3. Make sure the user cannot connect with themselves.
4. Let the user know when the connection is successful and when another peer connected with them.
5. Send a message to another peer using their connection id from the `list` command.
6. Receive messages by setting a server in another thread.
7. Print information based on what "type" of connection is made:
    - When a peer sends message.
    - When a peer establishes a connection.
    - When a peer terminates their connection.
8. Handle input from the user.
9. Update README.md

## Contribution made by Ayush Thapaliya
1. Display available commands by making `help`.
2. List connections and display them.
3. Terminate a connection using a connection id entered by the user.
4. When the user uses the `exit` command, terminate all connection from the list.
5. Make sure the program has accomplishes all project requirements.
6. Test and make sure program is working with no errors.

## Installation
Install the latest version of Python. The version we used for this project is 3.11.2.
Python modules such as `sys`, `_thread`, and `socket` should be included with Python installation.

## How to Run the Program
1. Open the terminal in the directory where chat.py is stored.
2. Make sure Python is installed by running `python --version`. The output should be `Python <version_number>`.
3. Enter `python chat.py <listening_port_number>` in the terminal.
4. After successfully running the command, use the `help` command to learn more how to use the program
