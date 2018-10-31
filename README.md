# Steganography_Batch_B
This repository contains the Data Compression and Encryption ISE component-2 on Steganography by,
* 2015120023 - Akash Mahale
* 2015120025 - Swapnil Masurekar
* 2015120033 - Prathamesh Pai
* 2015120035 - Vedanta Pawar

### System Architecture
![System Architecture](https://github.com/swapnil3597/Steganography_Batch_B/blob/master/Data/image.png)

#### Python libraries required:
- PyCrypto:  ```$ pip install pycrypto```

#### Repository Details:
* **Data folder:** Consists of Audio files, data to be hidden and public Keys in 'obj' folder.
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

## Acknowledgements

Mentor: **Dr. Preetida Jani**
This assignment is based on the paper, "A New Audio Steganography with Enhanced Security based on
Location Selection Scheme" by Shweta Vinayakarao Jadhav and Prof. A.M Rawate. For more details refer this [link](http://ijesc.org/upload/c15c8681fbc2fdde9ea423a359366306.A%20New%20Audio%20Steganography%20with%20Enhanced%20Security%20based%20on%20Location%20Selection%20Scheme.pdf)
