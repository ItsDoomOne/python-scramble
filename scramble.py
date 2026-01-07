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

def fancy_exit(text):
	print(text)
	sys.exit()

try:
	if not len(sys.argv) == 3:
       fancy_exit("You need to provide exactly two arguments.")
	if not sys.argv[1].casefold() in ["s", "d", "scramble", "descramble"]
	   fancy_exit("The first argument needs to be 's', 'd', 'scramble' or 'descranble'")
	if not os.path.isfile(sys.argv[2]):
	   fancy_exit("The secound argument must be a valid file path.")
	if sys.argv[1].casefold() in ["s", "scramble"]:
		f = open(sys.argv[2], 'r')
		text = f.read()
		scramble(text, sys.argv[2])
	else:
		F = open(sys.argv[2], 'r')
		text = []
		text = F.read()
		descramble(sys.argv[2], 'r')
				
except:
	fancy_exit("Code has exited for some unknown reason. This is still being implemented.")
	

