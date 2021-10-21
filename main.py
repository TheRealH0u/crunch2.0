#!usr/bin/env python3.10
from sys import argv
from sys import exit


def error(errorNum):
	match errorNum:
		case 0:
			print("ERROR: One to many arguments")
		case 1:
			print("ERROR: ONLY CHARACTERS. For now")
		case 2:
			print("ERROR: No arguments")
	exit(1)

def main():
	#Say hello
	print("Crunch2.0")

	args = argv[1:]
	#Check if no arguments
	if len(args) == 0:
		error(2)
	#Check if only one argument
	if len(args) > 1:
		error(0)
		
	#second check if only characters
	for char in args[0]:
		if char.isdigit():
			error(1)

	print("-Ok lets start-")

	# All characters specified as arguments into array
	ar = []
	for char in args[0]:
		ar.append(char.lower())

	# Print lenght of wordlist 2**(number of letters)
	print("Length of wordlist: ", 2**len(ar))

	#ok so now we do the math 2^(number of letters)

	binary = "0"*len(ar)
	for i in range(int((2**len(ar)))):
		arr = []
		for d in binary:
				arr.append(int(d))
		for a in range(len(ar)):
			try:
				if(arr[a] == 1):
					print(ar[a].upper(), end = "" )
				else:
					print(ar[a], end = "" )
			except:
				print(ar[a], end = "" )
		print("")
		binary = int(binary, 2) + int("1", 2)
		#matej 5 - 1 - 1 = 3
		binary = str(bin(binary)[2:].zfill(len(ar)-(len(str(binary))-1)))

#This at the end
if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print("ERROR: {}".format(e))


