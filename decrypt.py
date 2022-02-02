from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


if __name__ == "__main__":
    print("Here is your decryption key.")
    private_key = RSA.import_key(open("private.pem").read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    with open("aes_key.txt", "rb") as file:
        content = file.read()
    decrypted_content = cipher_rsa.decrypt(content)
    with open("aes_key.txt", "wb") as file2:
        file2.write(decrypted_content)
    with open("aes_key.txt", "rb") as file3:
        key = file3.read()
        print(key.decode())
