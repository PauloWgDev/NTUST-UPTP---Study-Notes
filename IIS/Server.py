# Server

from queue import Full
import socket
import threading
import DES


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
chat_terminated = "6969000000000000"


# Functions for Encryption/Decryption and Padding

def DES_encrypt(message, _key):
    if (len(message) < 16):
        message = pad_message(message)
    encrypted_message = DES.performDES(message, _key, 0)
    return encrypted_message

def DES_decrypt(message, _key):
    decrypted_message = DES.performDES(message, _key, 1)
    return decrypted_message

def pad_message(message):
    padding_length = 16 - len(message) % 16
    padding = '0' * padding_length
    padded_message = message + padding
    return padded_message


def double_DES_encrypt(message, _key):
    encrypted_message_phase_1 = DES_encrypt(message, _key)
    encrypted_message_phase_2 = DES_encrypt(encrypted_message_phase_1, _key)
    return encrypted_message_phase_2

def double_DES_decrypt(message, _key):
    decrypted_phase_1 = DES_decrypt(message, _key)
    decrypted_phase_2 = DES_decrypt(decrypted_phase_1, _key)
    print("\n[2-DES] decrypted phase 1: ", decrypted_phase_1)
    print("[2-DES] decrypted phase 2: ", decrypted_phase_2)
    return decrypted_phase_2

def triple_DES_encrypt(message, _key, _key2):
    encrypted_message_phase_1 = DES_encrypt(message, _key2)
    encrypted_message_phase_2 = DES_encrypt(encrypted_message_phase_1, _key)
    encrypted_message_phase_3 = DES_encrypt(encrypted_message_phase_2, _key)
    return encrypted_message_phase_3

def triple_DES_decrypt(message, _key, _key2):
    decrypted_phase_1 = DES_decrypt(message, _key2)
    decrypted_phase_2 = DES_decrypt(decrypted_phase_1, _key)
    decrypted_phase_3 = DES_decrypt(decrypted_phase_2, _key)
    print("\n[3-DES] decrypted phase 1: ", decrypted_phase_1)
    print("[3-DES] decrypted phase 2: ", decrypted_phase_2)
    print("[3-DES] decrypted phase 3: ", decrypted_phase_3)
    return decrypted_phase_3


def encrypt_message(message):
    match encryption_type:
        case 0:
            return DES_encrypt(message, key1)
        case 1:
            return double_DES_encrypt(message, key1)
        case 2:
            return triple_DES_encrypt(message, key1, key2)
    return DES_encrypt(message, key1)


def decrypt_message(message):
    match encryption_type:
        case 0:
            return DES_decrypt(message, key1)
        case 1:
            return double_DES_decrypt(message, key1)
        case 2:
            return triple_DES_decrypt(message, key1, key2)
    print("[ERROR] Incorrect encryption_type value")
    return DES_decrypt(message, key1)

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
            print("\n[" + str(connection.getpeername()) + "] Encrypted Message: ", message.decode())
            decrypted_message = decrypt_message(message.decode())
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
encryption_type = int(input("[SETUP] Select Encryption to use: "))

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
