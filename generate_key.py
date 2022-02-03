from Crypto.PublicKey import RSA


def generate_keys():
    key = RSA.generate(2048)
    privatekey = key.export_key()
    print(privatekey)
    with open("evil_private.pem", "wb") as file:
        file.write(privatekey)
    publickey = key.publickey().export_key()
    print(publickey)
    with open("evil_public.pem", "wb") as file:
        file.write(publickey)

if __name__ == "__main__":
    generate_keys()