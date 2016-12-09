import os

def run(**agrs):
	print "[*] In dirlister module."
	files = os.listdir(".")

	return str(files)