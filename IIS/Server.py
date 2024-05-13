# Server

from queue import Full
import socket
import threading
import Custom_Cipher


# Set up
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)  # Set timeout to 1 second
port = 1234
s.bind(('', port))
print("socket binded to %s" %(port))
s.listen(1024)

# Variables

key1 = "AABB09182736CCDD"
key2 = "6969BEBEFEA42042"
chat_terminated = "6969"

chatting = True
count = 0
encryption_type = 0
clients =[]

def handle_client(connection):
    global count
    global clients

    connected =  True
    welcome = "Thank you for connecting to the Chat Room. Encryption Type %s" %(encryption_type)
    connection.send(welcome.encode('utf-8'))
    clients.append(connection)

    while connected:
        message = connection.recv(1024)
        if message is not None:
            decrypted_message = ''
            if(encryption_type < 3):
                print("\n[" + str(connection.getpeername()) + "] Encrypted Message: ", message.decode())
                decrypted_message = DES_Encrypter.decrypt_message(message.decode())
            else:             
                print("\n[" + str(connection.getpeername()) + "] Encrypted Message: ", message.decode('latin-1'))
                decrypted_message = AES_Encrypter.decrypt(message, encryption_type)
            
            if decrypted_message == chat_terminated:
                print("\n\nTerminating chat with client" + str(connection.getpeername()) + "...")
                connected = False
                break
            print("[" + str(connection.getpeername()) + "] Decrypted Message: ", decrypted_message, end="\n\n")

            # Broadcast the message to all other clients
            for client in clients:
                if client != connection:
                    client.send(message)
    
    clients.remove(connection)
    global chatting 
    chatting = False
    connection.close()


print("[HINT] 0 for DES")
print("[HINT] 1 for 2-DES")
print("[HINT] 2 for 3-DES with two keys")
print("[HINT] 3 for AES with 124 key")
print("[HINT] 4 for AES with 192 key")
print("[HINT] 5 for AES with 256 key")
encryption_type = int(input("[SETUP] Select Encryption to use: "))

DES_Encrypter = Custom_Cipher.DES_Algorithm(key1, key2, encryption_type)
AES_Encrypter = Custom_Cipher.AES_Algorithm()

## Main Loop
while chatting:
    try:
        c, addr = s.accept()
        print("Got connection from ", addr)
        count = count + 1
        client_thread = threading.Thread(target=handle_client, args=(c,))
        client_thread.start()
    except socket.timeout:
        if not chatting and len(clients) == 0:
            break

s.close()
