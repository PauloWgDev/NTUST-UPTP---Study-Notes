# Encryption/Decryption Access
import os
import DES
import AES


# DES Encryption Class

class DES_Algorithm:

    key1 = "0123456789ABCDEF"
    key2 = "ABCDEF0123456789"
    encryption_type = 0

    def __init__(self, _key1, _key2, _encryption_type):
        self.key1 = _key1
        self.key2 = _key2
        self.encryption_type = _encryption_type

    def DES_encrypt(self, message, _key):
        encrypted_message = DES.performDES(message, _key, 0)
        return encrypted_message

    def DES_decrypt(self, message, _key):
        decrypted_message = DES.performDES(message, _key, 1)
        return decrypted_message

    def pad_message(self, message):
        if len(message) % 16 != 0:
            padding_length = 16 - (len(message) % 16)
            padding = '0' * padding_length
            message += padding
        return message

    def double_DES_encrypt(self, message, _key):
        encrypted_message_phase_1 = self.DES_encrypt(message, _key)
        encrypted_message_phase_2 = self.DES_encrypt(encrypted_message_phase_1, _key)
        return encrypted_message_phase_2

    def double_DES_decrypt(self, message, _key):
        decrypted_phase_1 = self.DES_decrypt(message, _key)
        decrypted_face_2 = self.DES_decrypt(decrypted_phase_1, _key)
        return decrypted_face_2

    def triple_DES_encrypt(self, message, _key, _key2):
        encrypted_message_phase_1 = self.DES_encrypt(message, _key)
        encrypted_message_phase_2 = self.DES_encrypt(encrypted_message_phase_1, _key)
        encrypted_message_phase_3 = self.DES_encrypt(encrypted_message_phase_2, _key2)
        return encrypted_message_phase_3

    def triple_DES_decrypt(self, message, _key, _key2):
        decrypted_phase_1 = self.DES_decrypt(message, _key2)
        decrypted_phase_2 = self.DES_decrypt(decrypted_phase_1, _key)
        decrypted_phase_3 = self.DES_decrypt(decrypted_phase_2, _key)
        return decrypted_phase_3

    def ToHEX(self, text):
        hex_string = ""
        for char in text:
            hex_string += format(ord(char), '02X')
        return hex_string

    def FromHEX(self, hex_string):
        binary_data = bytes.fromhex(hex_string)
        return binary_data.decode('latin-1')

    def text_to_blocks(self, text, size):
        hex_blocks = []
        for i in range(0, len(text), size):
            block = text[i:i+size]
            hex_blocks.append(block)
        return hex_blocks

    def encrypt_message(self, message):
        hex_blocks = self.text_to_blocks(message, 8)
        encrypted_blocks = []
        for block in hex_blocks:
            block_hex = self.ToHEX(block)
            block_padded = self.pad_message(block_hex)
            match self.encryption_type:
                case 0:
                    encrypted_blocks.append(self.DES_encrypt(str(block_padded), self.key1))
                case 1:
                    encrypted_blocks.append(self.double_DES_encrypt(str(block_padded), self.key1))
                case 2:
                    encrypted_blocks.append(self.triple_DES_encrypt(str(block_padded), self.key1, self.key2))
        return ''.join(encrypted_blocks)

    def decrypt_message(self, message):
        hex_blocks = self.text_to_blocks(message, 16)
        decrypted_blocks = []
        for block in hex_blocks:
            match self.encryption_type:
                case 0:
                    decrypted_blocks.append(self.DES_decrypt(block, self.key1))
                case 1:
                    decrypted_blocks.append(self.double_DES_decrypt(block, self.key1))
                case 2:
                    decrypted_blocks.append(self.triple_DES_decrypt(block, self.key1, self.key2))
        decrypted_text = ''.join(decrypted_blocks)
        return self.FromHEX(decrypted_text)
    
class AES_Algorithm:

    iv = b'.\x08a[\x1b\xc7h\xf2\xdaO\x1e\xd3\xf9\x0b\xa8-'
    masterKey_128 = b'U\x9cx9\x8d\xc8\xf7\x83\nM\x0fa|\xa6\x07:'
    masterKey_192 = b']\xc4x"oI\xf6\xcc:\xf6N\x07\xfe\xcd~rx\xa47K\xbfN\xebq'
    masterKey_256 = b'j\x1cx\x1f|^\x81\x95\xa4\xdc09y\xe3\x84\xa9\x9e\xa2C\xf7:\xf3\x8c\xa7`\xd5\xaaK\xa3p\xd2\x88'

    def encrypt(self, msg, keysize):
        encrypted_msg = ""
        match keysize:
            case 4: 
                encrypted_msg = AES.AES(master_key=self.masterKey_192).encrypt_cbc(msg.encode('latin-1'), self.iv)
                return encrypted_msg
            case 5:
                encrypted_msg = AES.AES(master_key=self.masterKey_256).encrypt_cbc(msg.encode('latin-1'), self.iv)
                return encrypted_msg
        encrypted_msg = AES.AES(master_key=self.masterKey_128).encrypt_cbc(msg.encode('latin-1'), self.iv)
        return encrypted_msg
    


    def decrypt(self, encrypted_msg, keysize):
        msg = ""
        match keysize:
            case 4:
                msg = AES.AES(self.masterKey_192).decrypt_cbc(encrypted_msg, self.iv)
                return msg
            case 5:
                msg = AES.AES(self.masterKey_256).decrypt_cbc(encrypted_msg, self.iv)
                return msg
        msg = AES.AES(self.masterKey_128).decrypt_cbc(encrypted_msg, self.iv)
        return msg


def test_DES():

    original_txt = "test, para ver si funca la wea"
    print("Original Text: ", original_txt)

    myDes = DES_Algorithm("0123456789ABCDEF", "0123456789ABCDEF", 0)

    encrypted_txt = myDes.encrypt_message(original_txt)

    print("Encrypted Text: ", encrypted_txt)

    decrypted_txt = myDes.decrypt_message(encrypted_txt)

    print("Decrypted txt: ", decrypted_txt)


def test_AES():

    original_txt = "hola "

    print("Original Text: ", original_txt)

    myAES = AES_Algorithm()

    encrypted_txt = myAES.encrypt(original_txt, 4)

    print("Encrypted Text: ", encrypted_txt)

    decrypted_txt = myAES.decrypt(encrypted_txt, 4)

    print("Decrypted txt: ", decrypted_txt)

#test_AES()



