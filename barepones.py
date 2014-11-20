import sys
from scipy.io import wavfile
import wave
import tempfile
import pdb
from numpy.fft import fft
import numpy as np
import os

def get_match_index(list1_max, l2):
	# Check if this max is present in l2, if so return the index in l2
	i = 0
	while i < len(l2):
		if abs(list1_max - np.amax(l2[i])) < 2000000:
			return i
		else:
			i += 1
	return -1


def matches(p1, p2, threshold):
	pdb.set_trace()
	# We determine if these two points are close enough, as per threshold
	return abs(p1 - p2) <= threshold

file1 = sys.argv[1]
file2 = sys.argv[2]

if file1.endswith('.mp3'):
	name = file1.rsplit('/', 1)[1] + '.wav'
	os.system("/course/cs4500f14/bin/lame --decode --silent {file} tmp/{new_name}".format(file=file1, new_name=name))
	file1 = "tmp/{name}".format(name=name)

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
j = 0
matches = 0
offset = 0

#pdb.set_trace()

def check_sequence(l1, l2):
	#Check to see if 5 seconds of l1 is in l2
	j = 0
	f1_len = len(l1)
	f2_len = len(l2)
	while j < f1_len-50:
		# This chunks match
		chunk_max = np.amax(f1_fft_chunks[j])
		# See if there is a match in the other list, else -1
		match_index = get_match_index(chunk_max, f2_fft_chunks)
		if match_index >= 0:
			# If there is a match, see if we have 5 seconds
			total_matches = 0
			i = 0
			# We check the remainder of the song for a match
			room_to_check = f2_len - match_index
			# We make p to leave a trail of bread crumbs
			p = j
			# We may want to have some give.  Allow some lenientcy
			slip = 37
			while i < room_to_check:
				# Get the chunk maxes
				f1_chunk_max = np.amax(f1_fft_chunks[p])
				f2_chunk_max = np.amax(f2_fft_chunks[match_index])
				if abs(f1_chunk_max - f2_chunk_max) < 2000000:
					total_matches += 1
					p += 1
					match_index += 1
					i += 1
					if total_matches == 50:
						print "Match"
						return True
				else:
					# We see if we have any more slips to use
					if slip:
						slip = slip - 1
						total_matches += 1
                                        	p += 1
                                        	match_index += 1
                                        	i += 1
                                        	if total_matches == 50:
                                                	print "Match"
                                                	return True
					else:	
						# We're out of luck
						j += 1
						break
			#If we exit the while loop, we didn't reach 5 seconds of matches
			#TODO: We can tell upfront if we know we won't have enough space
			j +=1 
		else:
			# If no matches, move on and check for more
			j += 1

	print "No match"
	return False
check_sequence(f1_fft_chunks, f2_fft_chunks)	
