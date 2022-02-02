from Crypto.PublicKey import RSA


def generate_keys():
    key = RSA.generate(2048)
    privatekey = key.export_key()
    print(privatekey)
    with open("private.pem", "wb") as file:
        file.write(privatekey)
    publickey = key.publickey().export_key()
    print(publickey)
    with open("public.pem", "wb") as file:
        file.write(publickey)

if __name__ == "__main__":
    generate_keys()