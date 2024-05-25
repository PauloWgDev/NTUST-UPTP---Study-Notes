
# Concepts

## Diffie Hellman Key Exchange

Usually to have a secure communication, a symmetric key is used. Basically both parts have a secrete key that they use to decrypt the messages and only them can read it.
Diffie Hellman is how you get that secret key.

Diffie Hellman does **not exchange the actual key** because this way everybody would know the secret key. **What Diffie Hellman really does is it exchange some public variables and combines that with some private variables so that both parts can generate the secret key**.  

Basically, The Diffie-Hellman Key Exchange allows two parties to establish a shared secret key over an insecure channel.

### How it works:

1. **Public Variables**: Two public variables are agreed upon by both parties: a large prime number \( p \) and a base \( g \), where \( g \) is a primitive root modulo \( p \).

2. **Private Variables**: 
   - **Alice** selects a private random number \( a \).
   - **Bob** selects a private random number \( b \).

3. **Public Key Calculation**:
   - **Alice** computes her public key as \( A = g^a \mod p \) and sends \( A \) to Bob.
   - **Bob** computes his public key as \( B = g^b \mod p \) and sends \( B \) to Alice.

4. **Shared Secret Calculation**:
   - **Alice** receives \( B \) from Bob and computes the shared secret \( s \) as \( s = B^a \mod p \).
   - **Bob** receives \( A \) from Alice and computes the shared secret \( s \) as \( s = A^b \mod p \).

Both Alice and Bob now have the same shared secret \( s \) because:

\[ s = (g^b \mod p)^a \mod p = g^{ab} \mod p \]
\[ s = (g^a \mod p)^b \mod p = g^{ab} \mod p \]

This shared secret can then be used as a symmetric key for encrypting and decrypting messages.


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/8fbc0433-a9a3-478f-9a9b-3dbe2dc74480)


## Man in the Middle Attack

The man in the middle attack is an attack for the Diffie Hellman Key Exchange. Both parts think that they have a direct connection but in reality, there is a third malicious entity that is intercepting all their messages.
![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/9551b1f4-5dd9-4d39-a9aa-b0ba81ff2865)



The way it works is as follows:

1. **Intercept Public Keys**:
   - **Eve** intercepts Alice's public key \( A \) intended for Bob.
   - **Eve** intercepts Bob's public key \( B \) intended for Alice.

2. **Eve's Public Keys**:
   - **Eve** generates her own private keys \( e_a \) and \( e_b \).
   - **Eve** computes her public keys \( E_a = g^{e_a} \mod p \) and \( E_b = g^{e_b} \mod p \).

3. **Substitute Public Keys**:
   - **Eve** sends her public key \( E_b \) to Alice, pretending it's from Bob.
   - **Eve** sends her public key \( E_a \) to Bob, pretending it's from Alice.

4. **Shared Secrets**:
   - **Alice** computes the shared secret using \( E_b \) (Eve's public key) as \( s_a = E_b^a \mod p \).
   - **Bob** computes the shared secret using \( E_a \) (Eve's public key) as \( s_b = E_a^b \mod p \).

5. **Eve's Shared Secrets**:
   - **Eve** computes the shared secret with Alice using \( A \) (Alice's public key) as \( s_a = A^{e_b} \mod p \).
   - **Eve** computes the shared secret with Bob using \( B \) (Bob's public key) as \( s_b = B^{e_a} \mod p \).

Now, Eve has established two different shared secrets: one with Alice and one with Bob. She can decrypt any message from Alice, re-encrypt it using her shared secret with Bob, and send it to Bob, and vice versa.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/f4481dc8-7406-4165-a0e3-3977fc2d110c)




# My Implementation:

## Diffie Hellman Key Exchange

In my implementation, the Diffie-Hellman Key Exchange protocol is utilized to establish a shared secret key between Alice and Bob over an insecure communication channel. Both Alice and Bob generate private random numbers, compute public values, exchange these public values, and then derive a shared secret key using their private and the received public values. This shared secret key is then used for a AES encryption on their communication.

#### Function that performs the key exchange and AES key generation:

```python
def dh_key_exchange():

    private_key = generate_private_random_number()

    print("my private key: ", private_key)

  

    recieved_public_key = int(s.recv(1024).decode())

    print("recieved public key: ", recieved_public_key)

  

    my_public_key = compute_dh_public_value(private_key)

    print("my public key: ", my_public_key)

    s.send(str(my_public_key).encode())

  

    shared_key = compute_shared_secret(recieved_public_key, private_key)

    print("shared secret key: ", shared_key)

  

    return shared_key
```

## Man in the Middle Attack

To simulate a Man-in-the-Middle (MITM) attack, I implemented  the script Eve.py as the intermediary, who intercepts the communication between Alice and Bob. Eve manipulates the key exchange process by intercepting the public keys exchanged between Alice and Bob and substituting them with her own public keys. This allows Eve to derive separate shared secret keys with both Alice and Bob, effectively spying on and altering their communication without their knowledge.

#### MITM:

This function performs the Man In the Middle Attack and returns the two shared keys generated.

```python
def mitm_attack(alice_conn, bob_conn):

    private_key_mitm_alice = generate_private_random_number()

    private_key_mitm_bob = generate_private_random_number()

  

    # Receive Bob's public key

    bob_public_key = int(bob_conn.recv(1024).decode())

    print("Bob's public key: ", bob_public_key)

  

    # Send MITM's fake public key to Alice (pretending to be Bob)

    mitm_public_key_bob = compute_dh_public_value(private_key_mitm_bob)

    print("Fake public key to Alice: ", mitm_public_key_bob)

    alice_conn.send(str(mitm_public_key_bob).encode())

  

    # Receive Alice's public key

    alice_public_key = int(alice_conn.recv(1024).decode())

    print("Alice's public key: ", alice_public_key)

  

    # Send MITM's fake public key to Bob (pretending to be Alice)

    mitm_public_key_alice = compute_dh_public_value(private_key_mitm_alice)

    print("Fake public key to Bob: ", mitm_public_key_alice)

    bob_conn.send(str(mitm_public_key_alice).encode())

  

    # Compute shared secrets

    shared_key_alice = compute_shared_secret(alice_public_key, private_key_mitm_bob)

    shared_key_bob = compute_shared_secret(bob_public_key, private_key_mitm_alice)

  

    print("Shared key with Alice: ", shared_key_alice)

    print("Shared key with Bob: ", shared_key_bob)

  

    # Create AES ciphers for communication

    aes_alice = AES_Algorithm(hashlib.sha256(str(shared_key_alice).encode()).digest())

    aes_bob = AES_Algorithm(hashlib.sha256(str(shared_key_bob).encode()).digest())

  

    return aes_alice, aes_bob
```

#### Spy and Modify: 

This parts of the script receives the messages being send and lets you spy them and modify them if you want.

```python
encrypted_msg = src_conn.recv(1024)
if not encrypted_msg:
	print(f"No message received from connection. Closing.")
	break

print(f"Encrypted message : ", encrypted_msg.decode())

# Decrypt and re-encrypt the message
decrypted_msg = src_aes.decrypt(encrypted_msg.decode().encode('latin-1'))
print(f"Decrypted message : {decrypted_msg}")

# Modify the message
new_message = input("Insert the new message: ")

# If the new message is null, it will send the original message, otherwise it will send the modified message

if new_message == "" :      
	# send real message
	re_encrypted_msg = dst_aes.encrypt(decrypted_msg)
	dst_conn.send(re_encrypted_msg.decode('latin-1').encode())
else:
# send fake message
re_encrypted_msg = dst_aes.encrypt(new_message)
dst_conn.send(re_encrypted_msg.decode('latin-1').encode())
```

## Normal server vs Eve's server

In the scenario involving the normal server, communication between Alice and Bob occurs without any malicious interference and the server will only be able to see the encrypted text. In contrast, Eve's server actively conducts a MITM attack by intercepting and manipulating the key exchange process. By impersonating both Alice and Bob, Eve's server can decrypt, modify, and re-encrypt messages exchanged between Alice and Bob, effectively compromising the confidentiality and integrity of their communication.


### Using Normal Server:

##### Server Output:

Here the only thing that is not encrypted are the public keys that are sent at in the Diffie Hellman Key Exchange. All the rest of the communication is encrypted using AES so the server is only able to see the encrypted text.

```
Socket binded to 1234
Got connection from  ('127.0.0.1', 13781)  
Got connection from  ('127.0.0.1', 13804)  
13
7
Y-▲iö^#Þ☻lgßÌê
uèÂ»
∟ÙõìgvÅ
```

##### Alice Output:

```
my private key:  41
recieved public key:  13
my public key:  7
shared secret key:  2

hey!!
bob: what's up
```

##### Bob's Output:

```
my private key:  58
my public key:  13
recieved public key:  13
shared secret key:  2
alice: hey!!
what's up 
```


### Using Eve's Server:

Here eve's performs a MITM attack to spy and modify the messages between Alice and Bob.
In some point Bobs try to send the message `Hi!!`, but Eve's modifies that message and sends `I hate U` instead.
##### Eve's Output:


```
Socket binded to 1234
Got connection from Alice:  ('127.0.0.1', 14511)
Got connection from Bob:  ('127.0.0.1', 14519)
Bob's public key:  17
Fake public key to Alice:  6
Alice's public key:  2
Fake public key to Bob:  10
Shared key with Alice:  13
Shared key with Bob:  14

Encrypted message :  ªs'
‼^¨ öð→gM∟
Decrypted message : alice: Hello!!
Insert the new message:
Encrypted message :  `vuuS<4iÓáT\
Decrypted message : bob: Hi!!
Insert the new message: I hate U 
```

##### Alice Output:

```
my private key:  46
recieved public key:  6
my public key:  2
shared secret key:  13
Hello!!
I hate U
```

##### Bob's Output:

```
my private key:  73
my public key:  17
recieved public key:  17
shared secret key:  14
alice: Hello!!
Hi!!
```


# Observations and insights

After Implementing a Diffie-Hellman Key Exchange and then performing a MITM attack I got to some interesting conclusion.

First, I got to the conclusion that for a normal person it would be difficult to perform a MITM attack. The reason is that it would be very difficult to actually intercept the connection without making it too obvious.

Another conclusion I got is that although it is difficult to make a MITM attack for a normal person, for a server provider it would be extremely easy and the reason is that it is already the intermediary of the connection.  So the provider could make it seem that there is an encryption between the two parts but in reality it used a MITM to spy into all the messages.

