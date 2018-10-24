'''
This repository contains the Data Compression and Encryption ISE component-2 on Steganography by,

    2015120023 - Akash Mahale
    2015120025 - Swapnil Masurekar
    2015120033 - Prathamesh Pai
    2015120035 - Vedanta Pawar

'''

import os , sys
import wave , struct 
import binascii
import steganography


file = 'Data/1.wav'
text_file_name = 'Data/text_file.txt'
text_file = open(text_file_name, 'r') 
text = text_file.read()
text_file.close()


########################MAIN_CODE########################################
# text_bin = ' '.join(format(ord(x), 'b') for x in text) 
print(text)
text_bin = ''
for i in range(len(text)):
	char = text[i]
	char_bin = bin(ord(char))
	char_bin = char_bin[2:]
	if len(char_bin) < 7:
		char_bin = (7 - len(char_bin))*'0' + char_bin
	text_bin += char_bin
print(text_bin)

text_length = len(text_bin)
w = wave.open(file, mode = 'rb')
params = w.getparams()        # params = (nchannels, sampwidth, framerate, nframes, comptype, compname)
print(params)
bytes_original =  w.readframes(params[3])

frames = steganography.stegano_hide(w , bytes_original, text_bin)
w.close()
w_w = wave.open('Data/2.wav' , mode = 'wb')
steganography.create_wave(frames , params, w_w)
w_w.close()
w_w_r = wave.open('Data/2.wav' , mode = 'rb')
params = w_w_r.getparams()

w_r = wave.open('Data/2.wav' , mode = 'rb')
print(w_r.getparams())
recovere_text = steganography.extract_info(w_r, text_length)
w_r.close()

seeked_file = open('seeked_file.txt' , 'w')
seeked_file.write(recovere_text)
seeked_file.close()