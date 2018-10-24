# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:20:26 2018

@author: Swapnil Masurekar

Certificate Authority signs Bob's public Key and stores
the signature and its own public key in a text file
"""


from RSA_functions import *
import pickle

# Initializing Prime Numbers
p = 17
q = 19
print ("Generating Certificate Authority's public and private keypairs......")
public, private = generate_keypair(p, q) # CA's keys
print ("Certificate Authority's public key is ", public ," and Certificate Authority's private key is ", private)

# Store CA Public Key in pkl File
pickle_out = open("Data/obj/CA_public.pickle","wb")
pickle.dump(public, pickle_out)
pickle_out.close()
print("CA's public key written in pkl file")

# Certify Bob's Public Key
pickle_in = open("Data/obj/Bob_public.pickle","rb")
Bob_public = pickle.load(pickle_in)
Bob_certificate = encrypt(private, str(Bob_public))

# Store Bob's Certificate in pkl File
pickle_out = open("Data/obj/Bob_certificate.pickle","wb")
pickle.dump(Bob_certificate, pickle_out)
pickle_out.close()
print("Bob's public key certificate written in pkl file")
