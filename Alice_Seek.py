# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:20:26 2018

@author: Swapnil Masurekar, Vedanta Pawar, Akash Mahale, Prathamesh Pai

Alice gets Bob's Public Key from Trusted Authority
Then the AES Key from Bob is decrypted to get seek the info fro Audio
"""

from steganography_functions import *
from RSA_functions import *
import pickle
from Crypto.Cipher import AES
import os , sys
import wave , struct 
import binascii

# Read CA public key from text file
pickle_in = open("Data/obj/CA_public.pickle","rb")
CA_public = pickle.load(pickle_in)

# Read Bob's public key Certificate
pickle_in = open("Data/obj/Bob_certificate.pickle","rb")
Bob_certificate = pickle.load(pickle_in)
Bob_public_str = decrypt(CA_public, Bob_certificate)
Bob_public = eval(Bob_public_str)# Converting str to tuple
print("Bob's public key is being verified, Bob's Public key is", Bob_public)

# Read Bob's encrypted message
pickle_in = open("Data/obj/Bob_key_secure_channel.pickle","rb")
Bob_encrypted_msg = pickle.load(pickle_in)
print("AES Encryption Key Received")

# Decrypt Bob's message
(aes_key, text_len) = eval(decrypt(Bob_public, Bob_encrypted_msg))
print("The AES Key is: ", aes_key, "Text Length is: ", text_len)

# Seeking Encrypted text from the Audio
print("Steganography: Seeking Encrypted text from the Audio")
hidden_audio_file = 'Data/2.wav'
text_length = 500

w_r = wave.open(hidden_audio_file , mode = 'rb')
print(w_r.getparams())
recovered_text = extract_info(w_r, text_length)
w_r.close()

seeked_file = open('Data/seeked_file.txt' , 'w')
seeked_file.write(recovered_text[:text_len])
seeked_file.close()
print("Steganography: Encryped Data being seeked successfully")

# AES Decryption
decryption_suite = AES.new(aes_key, AES.MODE_CBC, 'This is an IV456')
plain_text = decryption_suite.decrypt(recovered_text[:text_len])
print("Data decrypted successfully")

# Recovered text from Audio
print("The Recovered text is: "+recovered_text[:text_len])