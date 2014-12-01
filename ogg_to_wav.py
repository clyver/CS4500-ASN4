import os
import sys
# takes an ogg file path and the path of the output
# creates new .wav file at out_path destination
# returns the outpath + .wav file as a string
def ogg_wav(ogg_file, out_path):
	try:
		os.system("oggdec -o {f1} {f2}".format(f1=out_path, f2=ogg_file))
	except IOError, e:
		print e

def endswith_ogg(file_path):
	if(file_path.endswith(".ogg")):
		return True
	else:
		return False

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print "does the file end with .ogg?"
endswith_ogg(arg1)
print "can we open the file as .ogg and convert to .wav?"
ogg_wav(arg1, arg2)
