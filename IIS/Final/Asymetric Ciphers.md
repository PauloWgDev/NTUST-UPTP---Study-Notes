# Asymetric Ciphers

Asymtric ciphers uses two keys, one public key and a private key, the public key is used for encryption and the private key is used for decryption.

P: plain text

C: cipher text

K<sub>private</sub>: private key

K<sub>public</sub>: public Key
</small>

C = encrypt(K<sub>public</sub>, P)

P = decrypt(K<sub>private</sub>, C)


The idea behind an asymetric Cipher is that you have two keys. One is your private key, this key is the one you will use to decrypt the messages, and then you have your public key which other people can use to encrypt the message.
So let's say you want to have a secure communication with someone. You will send him through the insecure channel the public key. The idea is that now this person can send you 
any message encrypting it using your public key and because you are the only one who has the private key related to that public key, you are the only one that can decrypt the message.
Once this other person has encrypted the message using the key you sent him, not even him can decrypt the cipher text generated.


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/b6353e9e-0ed9-41ae-8b5c-b4139948fd55)


## Knapsack Cryptosystem
