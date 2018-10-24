# Steganography_Batch_B
This repository contains the Data Compression and Encryption ISE component-2 on Steganography by,
* 2015120023 - Akash Mahale
* 2015120025 - Swapnil Masurekar
* 2015120033 - Prathamesh Pai
* 2015120035 - Vedanta Pawar

#### Python libraries required
- PyCrypto:  ```$ pip install pycrypto```

#### Repository Details:
* **Data folder:** Consists of Audio file and data to be hidden
* **Documentation_and_Resources:** Consists of Mini-project report and reference Research Paper.
* **steganography_functions.py:** Functions for Audio Steganography
* **RSA_functions.py:** Used for creating secure channel during Key-exchange
* **Bob_Hide.py:** The encypted message is hidden in Audio file and key is transferred via secured channel
* **Alice_Seek.py:** The hidden message is seeked and decrypted by Alice
* **CA.py:** Certificate Authority auhorizes Bob's Public Key

#### Execution Details:
```
$ python Bob_Hide.py
$ python CA.py
$ python Alice_Seek.py
```
