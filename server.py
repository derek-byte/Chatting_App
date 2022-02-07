# SERVER
import socket
import threading 

# 64 bytes 
HEADER = 64 
PORT = 3000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Runs concurently for each person
def handle_client(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected.")

  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    # Check is msg_length is not equal to None 
    if msg_length:
      msg_length = int(msg_length)
      # Nothing passes this line of code until it gets a message
      # Wait until something is sent over socket 
      msg = conn.recv(msg_length).decode(FORMAT)

      if msg == DISCONNECT_MESSAGE:
        connected = False 

      print(f"[{addr}] {msg}")
      conn.send("MSG Recieved".encode(FORMAT))
  conn.close()



def start_server():
  print("[STARTING] Server is starting...")
  server.listen()
  print(f"[LISTENING] Server is listening on {SERVER}")
  while True:
    # Will wait for new connection to server
    # Stores address and port and send info back 
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

