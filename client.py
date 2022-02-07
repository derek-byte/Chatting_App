import socket 
# import threading

# 64 bytes 
HEADER = 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# Set up socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connected to Server 
client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)

  # b ' ' is byte representation of this string 
  # We do this to meet the requirement of the msg being 64 bytes
  send_length += b' ' * (HEADER - len(send_length))
  client.send(send_length)
  client.send(message)
  print(client.recv(2048).decode(FORMAT))

def message():
  client_messaging = True 
  while client_messaging:
    print("Type 'disconnect' if you want to leave.")
    client_message = input()
    if client_message == "disconnect":
      send(DISCONNECT_MESSAGE)
    else:
      send(client_message)

def start_client():
  message()