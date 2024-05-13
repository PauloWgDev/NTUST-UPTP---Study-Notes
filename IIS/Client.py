# Client

import socket
import Custom_Cipher
import threading

# Variables

key = "AABB09182736CCDD"
key2 = "6969BEBEFEA42042"
chat = 1
encryption_type = 0

username = "username"

# Set up


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
s.connect(('127.0.0.1', port))


recieve = s.recv(1024).decode('latin-1')
print("[SERVER]: " + recieve)


username = input("\n[REGISTER] Choose a username: ")
username = ("[" + username + "] ")

print("Congratulations " + username + ", you are ready to start chatting.\n\n")

if (recieve == "Thank you for connecting to the Chat Room. Encryption Type 0"):
    encryption_type = 0
elif (recieve == "Thank you for connecting to the Chat Room. Encryption Type 1"):
    encryption_type = 1
elif (recieve == "Thank you for connecting to the Chat Room. Encryption Type 2"):
    encryption_type = 2
elif (recieve == "Thank you for connecting to the Chat Room. Encryption Type 3"):
    encryption_type = 3
elif (recieve == "Thank you for connecting to the Chat Room. Encryption Type 4"):
    encryption_type = 4
elif (recieve == "Thank you for connecting to the Chat Room. Encryption Type 5"):
    encryption_type = 5
else:
    encryption_type = 0


DES_Encrypter = Custom_Cipher.DES_Algorithm(key, key2, encryption_type)
AES_Encrypter = Custom_Cipher.AES_Algorithm()


# Function to continuously receive messages from the server
def receive_messages():
    while chat:
        try:
            encrypted_response = s.recv(1024)
            decrypted_response = (DES_Encrypter.decrypt_message(encrypted_response.decode('latin-1'))) if encryption_type < 3 else (AES_Encrypter.decrypt(encrypted_response, encryption_type))
            print(decrypted_response)
        except Exception as e:
            print("Error occurred:", e)
            break


# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main Loop
while(chat):
    msg = input()
    full_msg = (username + msg)

    if (encryption_type < 3):
        encrypted_msg = DES_Encrypter.encrypt_message(full_msg)
        s.send(encrypted_msg.encode())
    else:
        encrypted_msg = AES_Encrypter.encrypt(full_msg, encryption_type)
        # print("encrypt_msg: ", encrypted_msg)
        s.send(encrypted_msg)

    if (msg == "6969"):     # write 6969 to stop chatting
        s.send("6969".encode())
        chat = 0
        break

s.close()
