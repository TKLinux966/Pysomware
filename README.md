# Pysomware

This is a ransomware written in Python.

## How this ransomware works
#### generatekey.py
```
This script is for generateing public/private rsa key for encrypt/decrypt Fernet key used to encrypt files on your target machine.
You keep private.pem on your machine.
public.pem is used for encrypting files on yout target machine.
```
#### decrypt.py
```
This script is used for your target person(a victim) to get a decryption key for encrypted Ferner key.
```
#### ransom.py
```
This script is for encrypting all files on your target machine.
```

### Disclaimer
This is for educational purposes only. I'm not responsible for any trouble you cause with this malware.<br />
Bitcoin address comes from here (https://bitflyer.com/en-jp/s/glossary/address)<br />
Do NOT send bitcoin to this address.

## Before you try

I made this ransomware to learn how ransomwares work. So this ransomware is not evil and awesome compared to real ransomwares in the wild.<br />
