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

### Concept

The knapsack uses the concept of Super Increasing Lists to encrypt and decrypt messages.
A super Increasing list is a list in which each item on the list is greater than the sum of the previous numbers.

Example of Super Increasing List: [5, 10, 20, 40]

40 > (5 + 10 + 20)

20 > (5 + 10)

10 > 5




### My Implementation of Knapsack Encryption

#### Code:

##### Generate Keys

```python
def generateKeys(size):
    privateKey = generateSuperIncreasingList(size)

    # Generate Modulus, m > sum(privateKey)
    m = sum(privateKey) + random.randint(1, 100)

    # Find a coprime of m 
    r = 1
    while True:
        r = random.randint(2, m - 1)
        if gcd(m, r) == 1:
            break

    publicKey = generate_public_key(privateKey, m, r)
    
    return privateKey, publicKey, m, r
```

##### Encrypt 

```python
def Encrypt(publicKey, message):
    return knapsackSum(publicKey, message)
```

##### Decrypt

```python
def Decrypt(privateKey, m, r, cipher):
    # Calculate the modular inverse of r mod m
    rInverse = modInverse(r, m)
    # Multiply the cipher by the modular inverse of r, then take mod m
    s = (cipher * rInverse) % m
    print("s: ", s)
    # Use the super-increasing sequence (private key) to decode the message
    plain = inv_knapsackSum(s, privateKey)
    return plain
``` 

#### Testing/Output

##### Testing 

```python
def test():

    #Alice
    alice_privateKey, alice_publicKey, m, r = generateKeys(5)
    print("--- Alice ---") 
    print("private key: ", alice_privateKey) 
    print("Modulus: ", m) 
    print("Modulus Relative Prime: ", r)
    print("public key: ", alice_publicKey)  

    #Bob
    print("\n--- Bob ---") 
    message = [1, 0, 0, 1, 1]
    cipher = Encrypt(alice_publicKey, message)
    print("Encryption Key: ", alice_publicKey)
    print("Message: ", message)
    print("Cipher text: ", cipher)

    print("\n--- Alice ---")
    print("Recieved Cipher message: ", cipher)
    plain = Decrypt(alice_privateKey, m, r, cipher)
    print("Decrypted Message: ", plain)
```

##### Output

```
--- Alice ---
private key:  [13, 39, 117, 351, 1053]
Modulus:  1638
Modulus Relative Prime:  911
public key:  [377, 1131, 117, 351, 1053]

--- Bob ---
Encryption Key:  [377, 1131, 117, 351, 1053]
Message:  [1, 0, 0, 1, 1]
Cipher text:  1781

--- Alice ---
Recieved Cipher message:  1781
s:  1417
Decrypted Message:  [1, 0, 0, 1, 1]

```

