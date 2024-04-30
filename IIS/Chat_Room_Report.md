
# Introduction

This project consists of a chat room that allows multiple users to communicate to each other.
The communication between multiple users works using a server-client architecture. Each client connects securely to the server, encrypting messages using DES algorithms. The server then broadcasts these messages to all clients, and each client then decrypts the received message. When the server is started, users can select if they want to use DES, 2-DES, or 3-DES for encryption.

# Design

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/d7d1142b-6df9-48e1-bafb-7e105fa4d799)


The chat room consists of two main components: the server and the clients.

- **Server**: The server is responsible for handling incoming connections from clients, managing multiple client connections concurrently, sending and receiving messages to and from clients, and encrypting and decrypting messages using DES encryption algorithms.
    
- **Client**: The client connects to the server, sends messages to the server, receives messages from the server, and encrypts and decrypts messages using the same encryption algorithms as the server.

# Implementation
#### **Socket Programming**:

Both the server and client utilize the `socket` module in Python to establish network connections and communicate over TCP/IP.    
### Encryption Algorithms:

The base of the code for the DES algorithm I got it from [geeks4geeks](https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/) but I had to further modify these code to properly fit my needs.


 ##### **DES Algorithm**: 
 The Data Encryption Standard (DES) algorithm is implemented for basic encryption and decryption of messages.
 
```python
def DES_encrypt(message, _key):

    if (len(message) < 16):

        message = pad_message(message)

    encrypted_message = DES.performDES(message, _key, 0)

    return encrypted_message
```
  
  
##### **2-DES Algorithm**: 
Two iterations of the DES algorithm are performed consecutively to enhance security.

```python
def double_DES_encrypt(message, _key):
    encrypted_message_phase_1 = DES_encrypt(message, _key)
    encrypted_message_phase_2 = DES_encrypt(encrypted_message_phase_1, _key)
    return encrypted_message_phase_2
```

##### **3-DES Algorithm with Two Keys**: 
Three iterations of the DES algorithm are performed using two distinct keys, further strengthening the encryption process.

```python
def triple_DES_encrypt(message, _key, _key2):
    encrypted_message_phase_1 = DES_encrypt(message, _key2)
    encrypted_message_phase_2 = DES_encrypt(encrypted_message_phase_1, _key)
    encrypted_message_phase_3 = DES_encrypt(encrypted_message_phase_2, _key)
    return encrypted_message_phase_3
```



### Multithreading

On the server side, the application employs multithreading to handle multiple client connections simultaneously. Each client connection is managed by a separate thread on the server.

Meanwhile, and on the client side, multithreading is utilized to handle the reception of messages one thread and the sending of messages on another thread. This approach enables continuous and uninterrupted interaction between the client and server without blocking operations.


# Outputs:

### Server Set Up

The first output you get when running the Server.py script is the shown output, here you can select what kind of DES algorithm you want to use. If you enter 0, you will use the basic DES algorithm, if you enter 1 you will use the 2-DES algorithms and if you enter 2 you will use the 3-DES algorithm. And if you enter anything else the program will handle that by giving printing that the inserted value is not valid and will proceed to use the DES for encryption.


output:
```
DES Encription> & C:/Users/paulo/AppData/Local/Microsoft/WindowsApps/python3.11.exe "d:/UPTP-NTUST Books/Security/Homework 2 - Chat Console with DES Encription/Server.py"


DES: Thank for using DES encryption services :)


socket binded to 1234
[HINT] 0 for DES
[HINT] 1 for 2-DES
[HINT] 2 for 3-DES with two keys
[SETUP] Select Encryption to use:
```

### Clients connects to Server


Server output indicates connections established by clients, displaying their respective IP addresses and ports.

```
Got connection from  ('127.0.0.1', 9585)
Got connection from  ('127.0.0.1', 9893)
```

When clients connect to the server, they receive a welcome message indicating the encryption type being used.

```
[SERVER]: Thank you for connecting to the Chat Room. Encryption Type 0 
```

### Client send Message using encryption 3-DES

client 1 inputs 'ABCDABCDABCDABCD' on console:
```
ABCDABCDABCDABCD
```


The server shows the decryption process:
```
[3-DES] decrypted phase 1:  1EEE233E4CCB6C75
[3-DES] decrypted phase 2:  B9090C374D5DA61E
[3-DES] decrypted phase 3:  ABCDABCDABCDABCD
[('127.0.0.1', 10268)] Decrypted Message:  ABCDABCDABCDABCD
```

Client 2 recieves the following message:
```
[Anonymous User]:  ABCDABCDABCDABCD
```

### Client Disconnects from the chat room

To disconnect from the server, clients have to write 6969
```
6969
```

server output:
```
Terminating chat with client('127.0.0.1', 10283)...
```



