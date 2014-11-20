import sys
from scipy.io import wavfile
import wave
import tempfile
import pdb
from numpy.fft import fft
import numpy as np
import os

def matches(p1, p2, threshold):
	# We determine if these two points are close enough, as per threshold
	return abs(p1 - p2) <= threshold

file1 = sys.argv[1]
file2 = sys.argv[2]

if file1.endswith('.mp3'):
	name = file1.rsplit('/', 1)[1] + '.wav'
	os.system("/course/cs4500f14/bin/lame --decode --silent {file} tmp/{new_name}".format(file=file1, new_name=name))


f = wave.open(file1, 'rb')
nframes = f.getnframes()
frames  = f.readframes(nframes)
f.close()
temp = tempfile.NamedTemporaryFile(dir="/tmp/")
ft = wave.open(temp, 'wb')
ft.setparams((1, 2, 44100, nframes, "NONE", "not compressed"))
ft.writeframes(frames)
ft.close()

f2 = wave.open(file2, 'rb')
nframes2 = f2.getnframes()
frames2 = f2.readframes(nframes2)
f2.close()
temp2 = tempfile.NamedTemporaryFile(dir="/tmp/")
ft2 = wave.open(temp2, 'wb')
ft2.setparams((1, 2, 44100, nframes2, "NONE", "not compressed"))
ft2.writeframes(frames2)
ft2.close()

f1_sample_rate, f1_wav_data = wavfile.read(temp.name)
f2_sample_rate, f2_wav_data = wavfile.read(temp2.name)

#pdb.set_trace()
# We assume the songs are the same length
# Partition our file up into chunks 4096 long
f1_chunked = list(zip(*[iter(f1_wav_data)]*4096))
f2_chunked = list(zip(*[iter(f2_wav_data)]*4096))

f1_fft_chunks = []
f2_fft_chunks = []

#def wavdata_to_hz(data):
#	return abs(data * 441000) / 100000

#count = 0
for chunk in f1_chunked:
	fft_chunk = fft(chunk)
#	for f in fft_chunk:
#		fft_chunk[count] = wavdata_to_hz(f)
#		count += 1
	f1_fft_chunks.append(fft_chunk)
	
#count2 = 0
for chunk2 in f2_chunked:
	fft_chunk2 = fft(chunk2)
#	for f in fft_chunk2:
#		fft_chunk2[count2] = wavdata_to_hz(f)
#		count2 += 1
	f2_fft_chunks.append(fft_chunk2)

num_errors = 0
num_match = 0
i = 0
j = 0
matches = 0
offset = 0
#pdb.set_trace()
while i < len(f1_chunked):	
	x = np.amax(f1_fft_chunks[i])
	y = np.amax(f2_fft_chunks[j])
	f (abs(x - y) < 2000000):
		matches += 1
		offset += 1
		# Check next set of chunks
		while (i + offset < len(f1_chunked)):
			if (abs(np.amax(ff1_fft_chunks[i+offset]) - np.amax(f2_fft_chunks[j+offset])) < 2000000):
				matches += 1
			else:
				matches = 0
				# reset pointer offsets
	i += 1
		
			
	#dist = np.linalg.norm(x-y)
	#difmaxes = abs(np.amax(x) - np.amax(y))
#	for chunk in f2_fft_chunks:
		#print matches
#		if (abs(x - np.amax(chunk)) < 2000000):
#			matches += 1
#			break
			

#	if matches == 50:
#		print "MATCH: FIXME"
#		break
#	matches = 0
#	i+=1

#	if difmaxes < 2000000:
	#	print "dif between x and y maxes: {maxdif}".format(maxdif = np.amax(x) - np.amax(y))
#		num_match += 1
#	else:
	#	print "dif between x and y maxes for erros: {mdif}".format(mdif = np.amax(x) - np.amax(y))
#		num_errors += 1
#	i += 1

#print "The number of errors: ", num_errors
#print "The number of matches: ", num_match
