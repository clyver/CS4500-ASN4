__author__ = 'christopherlyver'
from wavData import WavData
import pdb


class Compare():
    """
    This class contatins the utilities and methods needed to compare two
    wav files
    """
        
    def __init__(self, f1, f2, error_threshold):
	"""
	We take in two files and make them WavData objects 
	"""
	self.f1 =  WavData(f1)
	self.f1.get_frequencies()
	self.f1.make_mono()
 	self.f1.get_fft()
		
	self.f2 =  WavData(f2)
	self.f2.get_frequencies()
	self.f2.make_mono()
	self.f2.get_fft()

	self.limit = error_threshold

    def equal(self, freq1, freq2, deviation_limit):
	"""
	Return True if the two numbers are within a threshold of each other
	"""
	if abs(freq1 - freq2) <= deviation_limit:
		return True
	else:
		return False
	

    def naive_compare(self):
	"""		
	Do a simple comare of two files' mono frequencies
	We say the two songs are equal if they have less then 'limit' diffences
	"""
	limit = self.limit
	errors = 0

	f1_noise = self.f1.frequencies 
	f2_noise = self.f2.frequencies 
	# Right now we assume the lengths of the songs are the same
	i = 0

	# We can optimize this by not continuing once we have reached our limit
	# rather than always going over the whole song if different. 
	while  i < len(f1_noise) and errors < limit:
		if not self.equal(f1_noise[i], f2_noise[i], limit):
	         	errors += 1
		i += 1
	if errors > limit:
		print "These songs are not the same, Bub"
		return False

	else:
		print "These songs are the same, Bub"
		return True

