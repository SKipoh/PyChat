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

def on_closing(event=None):
    #Function called when the window is closed
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
#For the messages to be sent
my_msg = tkinter.StringVar()
my_msg.set("Type your messages here")
#A scrollbar to navigate through the chat
scrollbar = tkinger.Scrollbar(messages_frame)

msg_list = tkinter.Listbox(messages_frame, height=15, width=50), yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack

messages_frame.pack()