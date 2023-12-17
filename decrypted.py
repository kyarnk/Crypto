from Crypto.Cipher import DES

def decrypt_text(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext).decode('utf-8')
    return decrypted_text.rstrip()
def main():
    with open("encryptedtext.txt", 'rb') as file:
        ciphertext = file.read()
    with open("key.txt", 'rb') as file:
        key = file.read()
    decrypted_text = decrypt_text(key, ciphertext)
    with open("decryptedtext.txt", 'w') as file:
        file.write(decrypted_text)
    print("DECRYPTED")
if __name__ == '__main__':
    main()
