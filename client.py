#! python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

def receive():
    #Handles receiving of messages
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break

def send(event=None):
    #Handles sending messages
    msg = my_msg.get()
    #Clears Input Field
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()