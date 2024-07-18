import threading
import socket
import argparse
import os
import sys
import tkinter as tk

class Send(threading.Thread):
    # Listens for user input from command line

    # sock: the connected socket object
    # name (str): The username provided by the user

    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name

    def run(self):
        # Listens to the user input and send it to the server
        # Typing "QUIT" will close the connection and exit the app

        while True:
            print('{}: '.format(self.name), end='')
            sys.stdout.flush()
            message = sys.stdin.readline()[:-1]

            # If we press "QUIT" we leave the chatroom
            if message == "QUIT":
                self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
                break

            # Send message to server for broadcasting
            else:
                self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))

        print('\nQuitting...')
        self.sock.close()
        os._exit(0)

class Receive(threading.Thread):
    # Listens for incoming messages from the server

    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name
        self.messages = None

    def run(self):
        # Receives the data from the server and displays it in the GUI
        while True:
            message = self.sock.recv(1024).decode('ascii')
            if self.messages:
                self.messages.insert(tk.END, message)
                print('\r{}\n{}:'.format(message, self.name), end='')
            else:
                print('\r{}\n{}:'.format(message, self.name), end='')

class Client:
    # Manages the client-server connection and integrates the GUI

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = None
        self.messages = None

    def start(self):
        print('Trying to connect to {}:{}...'.format(self.host, self.port))

        self.sock.connect((self.host, self.port))

        print('Successfully connected to {}:{}'.format(self.host, self.port))
        print()

        self.name = input('Your name: ')
        print()
        print('Welcome, {}! Getting ready to send and receive messages...'.format(self.name))

        # Creating send and receive threads
        send = Send(self.sock, self.name)
        receive = Receive(self.sock, self.name)

        # Starting the threads
        send.start()
        receive.start()

        self.sock.sendall('Server: {} has joined the chat. Say what\'s up!'.format(self.name).encode('ascii'))
        print("\rReady! Leave the chatroom anytime by typing 'QUIT'\n")
        print('{}: '.format(self.name), end='')

        return receive

    def send(self, textInput):
        # Send textInput data from the GUI
        message = textInput.get()
        textInput.delete(0, tk.END)
        self.messages.insert(tk.END, '{}: {}'.format(self.name, message))

        # Type 'QUIT' to leave the chatroom
        if message == "QUIT":
            self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
            print('\nQuitting...')
            self.sock.close()
            os._exit(0)

        # Send the message to the server for broadcasting
        else:
            self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))

def main(host, port):
    # Initializing and running the GUI application

    client = Client(host, port)
    receive = client.start()

    window = tk.Tk()
    window.title("Desktop Chat Application")

    fromMessage = tk.Frame(master=window)
    scrollbar = tk.Scrollbar(master=fromMessage)
    messages = tk.Listbox(master=fromMessage, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
    messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    client.messages = messages
    receive.messages = messages

    fromMessage.grid(row=0, column=0, columnspan=2, sticky="nsew")
    fromEntry = tk.Frame(master=window)
    textInput = tk.Entry(master=fromEntry)

    textInput.pack(fill=tk.BOTH, expand=True)
    textInput.bind("<Return>", lambda x: client.send(textInput))
    textInput.insert(0, "Write your message here.")

    Sendbtn = tk.Button(
        master=window,
        text='Send',
        command=lambda: client.send(textInput))

    fromEntry.grid(row=1, column=0, padx=10, sticky="ew")
    Sendbtn.grid(row=1, column=1, padx=10, sticky="ew")

    window.rowconfigure(0, minsize=500, weight=1)
    window.rowconfigure(1, minsize=50, weight=0)
    window.columnconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=200, weight=0)

    window.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chatroom Client")
    parser.add_argument('host', help='Interface the client connects to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')

    args = parser.parse_args()

    main(args.host, args.p)
