# Pysomware

This is a ransomware written in Python. It only works for Windows.

### Disclaimer
This is for educational purposes only. I'm not responsible for any trouble you cause with this malware.<br />
Bitcoin address comes from here (https://bitflyer.com/en-jp/s/glossary/address)<br />
Do NOT send bitcoin to this address.

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

## Before you try
I made this ransomware to learn how ransomwares work. So this ransomware may not be evil and great compared to real ransomwares in the wild.<br />
I left some functions uncommented or undeleted because of debugging purpose. You can uncomment or delete them for sure.
