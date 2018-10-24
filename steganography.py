import os , sys
import wave , struct 
import binascii

file = '1.wav'
text_file_name = 'text_file.txt'
text_file = open('text_file.txt', 'r') 
text = text_file.read()
text_file.close()


###############HIDE DATA IN AUDIO ###########################################
def stegano_hide(w , bytes_original, text_bin):
	glob_counter = 0
	(nchannels, sampwidth, framerate, nframes, comptype, compname) = w.getparams()
	bytes_steg = ''
	if(nframes%2!=0):
		bytes_original = bytes_original[0:len(bytes_original)-1]
	for i in range(len(bytes_original)/2-1):
		bite = bytes_original[2*i:2*i+2]
		msb_bite_bin = bin(ord(bite[1]))
		if len(msb_bite_bin)<10:
			msb_bite_bin = msb_bite_bin[2:]
			for j in range(8-len(msb_bite_bin)):
				msb_bite_bin = '0' + msb_bite_bin
			msb_bite_bin = '0b' + msb_bite_bin
			# print(msb_bite_bin)
		col_dig = msb_bite_bin[len(msb_bite_bin)-5:len(msb_bite_bin)-2]
		col_number = int(col_dig , 2)
		lsb_bite_bin = bin(ord(bite[0]))
		if len(lsb_bite_bin)<10:
			lsb_bite_bin = lsb_bite_bin[2:]
			for j in range(8-len(lsb_bite_bin)):
				lsb_bite_bin = '0' + lsb_bite_bin
			lsb_bite_bin = '0b' + lsb_bite_bin
		lsb_bite_bin = lsb_bite_bin[2:]
		msb_bite_bin = msb_bite_bin[2:]
	
		if glob_counter < len(text_bin):
			lsb_bite_bin = list(lsb_bite_bin)
			if text_bin[glob_counter] == '1':
				lsb_bite_bin[7-col_number] = 1
			else:
				lsb_bite_bin[7-col_number] = 0
			glob_counter += 1 
		else:
			pass

		lsb_bite_bin = ''.join(map(str, lsb_bite_bin))
		
		lsb_bite_bin = '0b' + lsb_bite_bin
		lsb_bite_bin = chr(int(lsb_bite_bin , 2))
		msb_bite_bin = ''.join(msb_bite_bin)
		msb_bite_bin = '0b' + msb_bite_bin
		msb_bite_bin = chr(int(msb_bite_bin , 2))
		bytes_steg += lsb_bite_bin+msb_bite_bin
	print(len(bytes_steg),'In Encoding')
	return bytes_steg

##############CREATE AUDIO FILE WITH HIDDEN DATA######################################################
def create_wave(frames , params , w_w):
	w_w.setparams(params)
	w_w.writeframes(frames)
	return


##############EXTRACT HIDDEN DATA #############################################
def extract_info(w_r , frames, test_len):
	(nchannels, sampwidth, framerate, nframes, comptype, compname) = w_r.getparams()
	# print(nframes)
	bytes_hidden = w_r.readframes(nframes)
	decrypt_text = ''
	fin_decrypt_text = ''
	if(test_len%2 != 0):
		bytes_hidden = bytes_hidden[0:len(bytes_hidden)-1]
	for i in range(len(bytes_hidden)/2-1):
		bite = bytes_hidden[2*i:2*i+2]
		msb_bite_bin = bin(ord(bite[1]))
		if len(msb_bite_bin)<10:
			msb_bite_bin = msb_bite_bin[2:]
			for j in range(8-len(msb_bite_bin)):
				msb_bite_bin = '0' + msb_bite_bin
			msb_bite_bin = '0b' + msb_bite_bin
		col_dig = msb_bite_bin[len(msb_bite_bin)-5:len(msb_bite_bin)-2]
		col_number = int(col_dig , 2)
		lsb_bite_bin = bin(ord(bite[0]))
		if len(lsb_bite_bin)<10:
			lsb_bite_bin = lsb_bite_bin[2:]
			for j in range(8-len(lsb_bite_bin)):
				lsb_bite_bin = '0' + lsb_bite_bin
			lsb_bite_bin = '0b' + lsb_bite_bin
		lsb_bite_bin = lsb_bite_bin[2:]
		msb_bite_bin = msb_bite_bin[2:]
		decrypt_text += lsb_bite_bin[7 - col_number]

	for i in range(len(decrypt_text)/7):
		text = decrypt_text[7*i : 7*i+7]
		text = chr(int(text , 2))
		fin_decrypt_text += text
	print(fin_decrypt_text[:200])
	return 



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
# print(text_bin)

test_len = len(text_bin)
w = wave.open(file, mode = 'rb')
params = w.getparams()        # params = (nchannels, sampwidth, framerate, nframes, comptype, compname)
print(params)
bytes_original =  w.readframes(params[3])
print(len(bytes_original), 'Bytes Original')
# print(' '.join(format(ord(x),'b')) for x in bytes_original)

frames = stegano_hide(w , bytes_original, text_bin)
print(len(frames), 'In MAIN_CODE')
w.close()
w_w = wave.open('2.wav' , mode = 'wb')
create_wave(frames , params, w_w)

w_w.close()
w_r = wave.open('2.wav' , mode = 'rb')
print(w_r.getparams())
extract_info(w_r,frames, test_len)

w_r.close()
