import socket
import threading

HEADER = 64
PORT = 1338
SERVER = socket.gethostbyname(socket.gethostname())#bierze adres IP sieci i urządzenia
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr): #individual connection between server and client
    print("[NEW CONNECTION] {ADDR} CONECTED")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            
        
        print(f"[{addr}]{msg}")

    conn.close()
        
    
def start(): #handle new collection
    server.listen()
    while True:
        conn, addr = server.accept() #this line waits for a new connection to a server
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")
        
print("Server is starting...")
start()

