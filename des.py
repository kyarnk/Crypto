from Crypto.Cipher import DES
import os

def encrypt_text(key, plaintext):
 cipher = DES.new(key, DES.MODE_ECB)
 ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
 return ciphertext
def pad_text(text):
 while len(text) % 8 != 0:
     text += ' '
 return text
def main():
    with open("input.txt", 'r') as file:
        plaintext = file.read()
    with open("key.txt", 'rb') as file:
        key = file.read()
    plaintext = pad_text(plaintext)
    ciphertext = encrypt_text(key, plaintext)
    with open("encryptedtext.txt", 'wb') as file:
        file.write(ciphertext)
    print("Зашифровано")
if __name__ == '__main__':
    main()
