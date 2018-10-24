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


hidden_audio_file = 'Data/2.wav'
text_length = 150

w_r = wave.open(hidden_audio_file , mode = 'rb')
print(w_r.getparams())
recovered_text = steganography.extract_info(w_r, text_length)
w_r.close()

print(recovered_text)
seeked_file = open('seeked_file.txt' , 'w')
seeked_file.write(recovered_text)
seeked_file.close()