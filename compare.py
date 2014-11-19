__author__ = 'christopherlyver'
from wavData import WavData
import pdb
import numpy as np

class Compare():
    """
    This class contatins the utilities and methods needed to compare two
    wav files
    """
        
    def __init__(self, f1, f2, equal_threshold, alloted_diff):
	"""
	We take in two files and make them WavData objects 
	"""
	self.f1 =  WavData(f1)
	self.f1.get_duration()
	self.f1.make_mono()
	pdb.set_trace()
	self.f1.chunk(4096)
	wav_to_fft = np.array([])
	for chunk in self.f1.frequencies:
		fft_chunk = self.f1.get_rfft(chunk)
		wav_to_fft.append(fft_chunk)
	pdb.set_trace()
	self.f1.frequencies = wav_to_fft
	
	self.f2 =  WavData(f2)
	self.f2.get_duration()
	self.f2.make_mono()
	self.f2.chunk(4096)
	wav_to_fft = []
	for chunk in self.f2.frequencies:
                fft_chunk = self.f2.get_rfft(chunk)
                wav_to_fft.append(fft_chunk)

	self.f2.frequencies = wav_to_fft


	i = 0
	while i < len(self.f1.frequencies):
		print "f1: ", self.f1.frequencies[0][i], " f2: ", self.f2.frequencies[0][i]
		i += 1
	self.limit = alloted_diff
	self.deviation_limit = equal_threshold

    def equal(self, freq1, freq2):
	"""
	Return True if the two numbers are within a threshold of each other
	"""
	
	dist = np.linalg.norm(freq1-freq2)
	print "dist", dist	
	if dist <= self.deviation_limit:
		return True
	else:
		return False

	#if abs(freq1 - freq2) <= self.deviation_limit:
	#	return True
	#else:
	#		return False
	

    def compare(self):
	"""		
	Do a simple comare of two files' mono frequencies
	We say the two songs are equal if they have less then 'limit' diffences
	"""
 	pdb.set_trace()	
	# Do an intitial test to make sure the files are the same duration
	if self.f1.duration != self.f2.duration:
		#print "These songs are not the same duration, and thus differ"
		return False
	else:
		# They are the same duration, compare the samples
		
		limit = self.limit
		errors = 0
	
		f1_noise = self.f1.frequencies 
		f2_noise = self.f2.frequencies
		
		#print "f1_noise {f1}".format(f1 = f1_noise)
		#print "####################################"
		#print "f2_noise {f2}".format(f2 = f2_noise)
 
		# Right now we assume the lengths of the songs are the same

		ind0 = 0
		ind1 = 0
		# Go through the samples and check for diff. If diff += 1 errors
		for i in f1_noise:
			for j in f2_noise:
				# FOR TESTING PURPOSES
				#print "comparing {t1} with {t2}".format(t1=j, t2=f2_noise[ind0][ind1])
				if not self.equal(i, j):
		         		errors += 1
				if(ind1 == 1):
					ind1 -= 1
				else:
					ind1 += 1
			ind0 += 1
		
		# We've broken out of the loop due \
		# to completion or error limit reached
		# ^Figure out which one
		
		if errors < limit:	
			print "MATCH {f1} {f2}".format(f1=self.f1.short_name(), f2=self.f2.short_name())
			return True
