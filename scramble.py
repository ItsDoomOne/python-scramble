import os, sys

#text = raw_input("Write a phrase: ")
text_array = []
edit_array = []
new_array = []
de_array = []
alpha = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9', ' ', '\n', '.', ',', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
 'H', 'I', 'J', 'K', 'M', 'N', 'L', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X',
 'Y', 'Z', '-', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', ';',
 ':', '<', '>', '?', '/', '\\', '|']


def scramble(text, filename):
	print(text)
	outFile = os.path.join(os.path.dirname(filename), "(scrambled)"+os.path.basename(filename)) 
	for l in text:
		text_array.append(l)
	
	edit_array = text_array
	print(edit_array)
	
	for c in edit_array:
		num = alpha.index(c)
		new_array.append(num)

	clean = str(new_array)
	output = clean.translate("[,]")
	print(output)
	oF = open(outFile, 'w')
	oF.write(output)

def descramble(text):
	new_array = text.translate("[,]")
	print("secret code: " + str(new_array))
	for d in new_array.split(' '):
		intd = int(d)
		index = alpha[intd]
		de_array.append(index)
	output = ''.join(de_array)
	print(output)

try:
	if len(sys.argv) == 3:
		if sys.argv[1].casefold() in ["s", "d", "scramble", "descramble"] and os.path.isfile(sys.argv[2]):
			if sys.argv[1].casefold() in ["s", "scramble"]:
				f = open(sys.argv[2], 'r')
				text = f.read()
				scramble(text, sys.argv[2])
			else:
				#LOGIC FOR DESCRAMBLE
		else:
			print("It seems that you did not use 's' or 'd' as the first argument.")
			print("Correct syntax example: py scramble.py s <file_path>")
except:
	print("Code has exited for some unknown reason. This is still being implemented.")



option = input("Do you want to [S]cramble or [D]escramble? ")
if option == "scramble" or option == "S":
	file_scram = input("name of file to scramble: ")
	f = open(file_scram, 'r')
	text = f.read()
	scramble(text, file_scram)
elif option == "descramble" or option == "D":
	file_scram = input("name of the file to descramble: ")
	F = open(file_scram, 'r')
	text = []
	text = F.read()
	#print "text input: " + str(text)
	descramble(text)
else:
	#descramble(text)
	sys.exit(0)

