# Client

import socket
import DES
import threading

# Variables

key = "AABB09182736CCDD"
key2 = "6969BEBEFEA42042"
chat = 1
encryption_type = 0

# Set up

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
s.connect(('127.0.0.1', port))

recieve = s.recv(1024).decode('utf-8')
print("[SERVER]: " + recieve)

if (recieve == "Thank you for connecting to the Chat Room. Encryption Type 0"):
    encryption_type = 0
elif (recieve == "Thank you for connecting to the Chat Room. Encryption Type 1"):
    encryption_type = 1
elif (recieve == "Thank you for connecting to the Chat Room. Encryption Type 2"):
    encryption_type = 2
else:
    encryption_type = 0


# Functions for Encryption/Decryption and Padding

def DES_encrypt(message, _key):
    padded_message = pad_message(message)
    encrypted_message = DES.performDES(padded_message, _key, 0)
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
    decrypted_face_2 = DES_decrypt(decrypted_phase_1, _key)
    return decrypted_face_2

def triple_DES_encrypt(message, _key, _key2):
    encrypted_message_phase_1 = DES_encrypt(message, _key)
    encrypted_message_phase_2 = DES_encrypt(encrypted_message_phase_1, _key)
    encrypted_message_phase_3 = DES_encrypt(encrypted_message_phase_2, _key2)
    return encrypted_message_phase_3

def triple_DES_decrypt(message, _key, _key2):
    decrypted_phase_1 = DES_decrypt(message, _key2)
    decrypted_phase_2 = DES_decrypt(decrypted_phase_1, _key)
    decrypted_phase_3 = DES_decrypt(decrypted_phase_2, _key)
    return decrypted_phase_3



def encrypt_message(message):
    match encryption_type:
        case 0:
            return DES_encrypt(message, key)
        case 1:
            return double_DES_encrypt(message, key)
        case 2:
            return triple_DES_encrypt(message, key, key2)

def decrypt_message(message):
    match encryption_type:
        case 0:
            return DES_decrypt(message, key)
        case 1:
            return double_DES_decrypt(message, key)
        case 2:
            return triple_DES_decrypt(message, key, key2)


# Function to continuously receive messages from the server
def receive_messages():
    while chat:
        try:
            encrypted_response = s.recv(1024)
            decrypted_response = decrypt_message(encrypted_response.decode())
            print("[Anonymous User]: ", decrypted_response + "\n")
        except Exception as e:
            print("Error occurred:", e)
            break


# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main Loop
while(chat):
    msg = input()
    encrypted_msg = encrypt_message(msg)
    s.send(encrypted_msg.encode())

    if (msg == "6969"):     # write 6969 to stop chatting
        chat = 0
        break

s.close()
