#! python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def accept_incoming_connections():
    #Sets up handling for incoming clients
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave!"+
                            "Now type your name and press enter!",
                            "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

#Takes client socket as an argument
def handle_client(client):
    #Handles single client connection
    name = client.recv(BUFSIZ).decode("utf8"))
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8")):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

# prefix is the name for identification
def broadcast(msg, prefix=""):
    #Broadcasts messages to all the connected clients
    for sock in clients:
        sock.send(bytes(prefix, "utf8") +msg)

if __name__ == "__main__":
    #Listens for up to 5 maximum connections
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = thread(target=accept_incoming_connections)
    #Starts the infinite loop
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join
    SERVER.close()