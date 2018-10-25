# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:20:26 2018

@author: Swapnil Masurekar, Vedanta Pawar, Akash Mahale, Prathamesh Pai

Bob generates a private key and it is saved in a file
Bob encrypts and hides the message in the Audio file 
and sends the key through a secure channel
"""

from steganography_functions import *
from RSA_functions import *
import pickle
from Crypto.Cipher import AES
import os , sys
import wave , struct 
import binascii

# Reading text file
file = 'Data/1.wav'
text_file_name = 'Data/text_file.txt'
text_file = open(text_file_name, 'r') 
text = text_file.read()
text_file.close()
print("The Plaintext is: "+text)

# Initializing Prime Numbers for RSA key generation 
p = 17
q = 19
print ("Generating Bob's public and private keypairs for secure channel using RSA......")
public, private = generate_keypair(p, q) # Bob's Keys
print ("Bob's public key is ", public ," and Bob's private key is ", private)

pickle_out = open("Data/obj/Bob_public.pickle","wb")
pickle.dump(public, pickle_out)
pickle_out.close()
print("Bob's public key written in pkl file")

# Initializing AES Key
aes_key = 'This is a key123'

# AES Encryption of text file
encryption_suite = AES.new(aes_key, AES.MODE_CBC, 'This is an IV456')
cipher_text = encryption_suite.encrypt(text)
print("Text Data Encrypted")
# print("cipher_text", cipher_text)

# Hiding the message
print("Steganography: Hiding the text data in the Audio File")
text_bin = ''
for i in range(len(text)):
	char = text[i]
	char_bin = bin(ord(char))
	char_bin = char_bin[2:]
	if len(char_bin) < 7:
		char_bin = (7 - len(char_bin))*'0' + char_bin
	text_bin += char_bin

text_length = len(text_bin)
w = wave.open(file, mode = 'rb')
params = w.getparams()# params = (nchannels, sampwidth, framerate, nframes, comptype, compname)
print(params)
bytes_original =  w.readframes(params[3])

frames = stegano_hide(w , bytes_original, text_bin)
w.close()
w_w = wave.open('Data/2.wav' , mode = 'wb')
create_wave(frames , params, w_w)
w_w.close()
print("Steganography: Data being hidden successfully in 'Data/2.wav' ")

# Passing AES Key and Text length through a secure channel
Bob_encrypted_msg = encrypt(private, str((aes_key, len(text))))
print ("Bob's encrypted AES Key is: ")
print (''.join(map(lambda x: str(x), Bob_encrypted_msg)))

# Creating a secure channel for AES key exchange
print("Hidden data Audio file sent to Alice and Key Exhanged via secue channel")
pickle_out = open("Data/obj/Bob_key_secure_channel.pickle","wb")
pickle.dump(Bob_encrypted_msg, pickle_out)
pickle_out.close()
print("Bob's encrypted Key written in pkl file")

