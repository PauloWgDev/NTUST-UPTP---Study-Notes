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

### Concepts

#### Super Increasing List 

The knapsack uses the concept of Super Increasing Lists to encrypt and decrypt messages.
A super Increasing list is a list in which each item on the list is greater than the sum of the previous numbers.

Example of Super Increasing List: [5, 10, 20, 40]

40 > (5 + 10 + 20)

20 > (5 + 10)

10 > 5

#### Keys

##### Private Keys

- A Super Increasing List: `privateKey`
- A number greater than the sum of all items in `privateKey`: `m`
- A relative prime of `m`: `r`

##### Public Key

- A List calculated using the `privateKey`, `m` and `r`: `publicKey`

#### Functions

- Encrypt: Use the `publicKey` to encrypt the binary message.
- Decrypt: Use the `privateKey`, modulus `m`, and multiplier `r` to decrypt the ciphertext.


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



## RSA

### Concepts

You have a public key and a private key, you usually used the private key to sign something and verify it with the public key.

Public Keys: (e, n)
    e usually is 65537
    n = p*q where p and q are two random prime numbers

Private Key: d 


**In RSA, p and q must be at least 512 bits; n must be at least 1024 bits.**

Let us learn the mechanism behind the RSA algorithm : >> Generating Public Key: 

```
Select two prime no's. Suppose P = 53 and Q = 59.
Now First part of the Public key  : n = P*Q = 3127.
 We also need a small exponent say e : 
But e Must be 
An integer.
Not be a factor of Φ(n). 
1 < e < Φ(n), 
Let us now consider it to be equal to 3.
    Our Public Key is made of n and e
```
Generating Private Key: 
```
We need to calculate Φ(n) :
Such that Φ(n) = (P-1)(Q-1)     
      so,  Φ(n) = 3016
    Now calculate Private Key, d : 
d = (k*Φ(n) + 1) / e for some integer k
For k = 2, value of d is 2011.
```

Now we are ready with our – Public Key ( n = 3127 and e = 3) and Private Key(d = 2011) Now we will encrypt “HI”:
```
Convert letters to numbers : H  = 8 and I = 9
    Thus Encrypted Data c = (89e)mod n 
Thus our Encrypted Data comes out to be 1394
Now we will decrypt 1394 : 
    Decrypted Data = (cd)mod n
Thus our Encrypted Data comes out to be 89
8 = H and I = 9 i.e. "HI".

```

### Approaches to Attack RSA:

- Brute Force: trying all possible private keys.
- Mathematical Attacks: all approaches equivalent in effor to factoring the product of two primes.
- Chosen ciphertext attacks: This type of attack exploits properties of the RSA algorithm.
- Timing Attacks: depend on the running time of the decryption algorithm.
- Hardware fault-based attack: Involves inducing hardware faults in the processor that is generating digital signatures.




