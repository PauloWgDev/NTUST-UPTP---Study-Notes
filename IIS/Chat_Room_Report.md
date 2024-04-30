
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
 
```
def DES_encrypt(message, _key):

    if (len(message) < 16):

        message = pad_message(message)

    encrypted_message = DES.performDES(message, _key, 0)

    return encrypted_message
```
  
  
##### **2-DES Algorithm**: 
Two iterations of the DES algorithm are performed consecutively to enhance security.

```
def double_DES_encrypt(message, _key):
    encrypted_message_phase_1 = DES_encrypt(message, _key)
    encrypted_message_phase_2 = DES_encrypt(encrypted_message_phase_1, _key)
    return encrypted_message_phase_2
```

##### **3-DES Algorithm with Two Keys**: 
Three iterations of the DES algorithm are performed using two distinct keys, further strengthening the encryption process.

```
def triple_DES_encrypt(message, _key, _key2):
    encrypted_message_phase_1 = DES_encrypt(message, _key2)
    encrypted_message_phase_2 = DES_encrypt(encrypted_message_phase_1, _key)
    encrypted_message_phase_3 = DES_encrypt(encrypted_message_phase_2, _key)
    return encrypted_message_phase_3
```



### Multithreading

On the server side, the application employs multithreading to handle multiple client connections simultaneously. Each client connection is managed by a separate thread on the server.

Meanwhile, and on the client side, multithreading is utilized to handle the reception of messages one thread and the sending of messages on another thread. This approach enables continuous and uninterrupted interaction between the client and server without blocking operations.
