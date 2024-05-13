
# Report: Secure Chat Room with AES Encryption.
## 1. Introduction

The objective of this assignment was to implement a secure chat application that uses AES encryption and decryption with CBC mode to ensure secure communication between two parties using socket programming.

## 2. Design Overview

### Encryption Algorithm

The application utilizes the Advanced Encryption Standard (AES) algorithm, a symmetric key encryption technique, for securing communication. AES operates on fixed-size blocks of data and supports key sizes of 128, 192, and 256 bits. In this implementation, AES with CBC (Cipher Block Chaining) mode is employed to provide confidentiality and integrity.

Because I used the code of the previous homework about implementing a chat room with DES algorithms. The chat room also supports the use of DES encryption algorithms and when starting the server it let's you choose which encryption algorithms you would like to use.

Starting the server:
```
socket binded to 1234
[HINT] 0 for DES
[HINT] 1 for 2-DES
[HINT] 2 for 3-DES with two keys
[HINT] 3 for AES with 124 key
[HINT] 4 for AES with 192 key
[HINT] 5 for AES with 256 key
[SETUP] Select Encryption to use: 
```

### Key Exchange

Before initiating communication, Alice sends an invitation to Bob along with the chosen encryption key size (either 128, 192 or 256 bits) encrypted with the shared key using CBC mode. The shared key is established between Alice and Bob prior to communication.

```
[SERVER]: Thank you for connecting to the Chat Room. Encryption Type 5
```

### Implementation Components

The application consists of two main components:

1. **AES Encryption and Decryption:**  The AES algorithm performs encryption and decryption of messages exchanged between the clients. Key expansion, substitution, shifting, mixing columns, and XOR operations are employed according to AES specifications.
2. **Socket Programming:** Socket programming is utilized to establish a connection between clients for message exchange. TCP/IP sockets are employed to enable reliable communication over a network.
   
   Example of clients communicating through the network:

Server:
```
[('127.0.0.1', 62631)] Encrypted Message:  Ö}0Ê3¾¢¦âÈ¿°↕Z9
[('127.0.0.1', 62631)] Decrypted Message:  [Alice] hey


[('127.0.0.1', 63984)] Encrypted Message:  0È5ê^{∟ôßþó+e{O
[('127.0.0.1', 63984)] Decrypted Message:  [Bob] hello!!
```

Client 1 (Alice): 
``` 
hey
[Bob] hello!!
```

Client 2 (Bob):
```
[Alice] hey
hello!!
```

## Security Measures

### Confidentiality

AES encryption with CBC mode ensures the confidentiality of messages exchanged between Alice and Bob. Each message block is encrypted using the shared key and the previous ciphertext block, preventing unauthorized access to the plaintext.

### Integrity

By encrypting the message blocks with a shared key, the integrity of the communication is maintained. Any tampering with the ciphertext would result in decryption errors, indicating potential unauthorized modifications.

### Key Security

The shared key used for encryption and decryption is crucial for maintaining security. Proper key management practices, including key exchange protocols and key size considerations, are essential to prevent key compromise and ensure long-term security.

## Conclusion

I think this assignment was useful to learn how to make a simple server-client connection architecture and also to know how you would implement the different encryption methods in a network.
