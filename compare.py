__author__ = 'christopherlyver'
from wavData import WavData


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
	self.f1.get_frequencies()
	self.f1.get_duration()
	self.f1.make_mono()
		
	self.f2 =  WavData(f2)
	self.f2.get_frequencies()
	self.f2.get_duration()
	self.f2.make_mono()

	self.limit = alloted_diff
	self.deviation_limit = equal_threshold

    def equal(self, freq1, freq2):
	"""
	Return True if the two numbers are within a threshold of each other
	"""
	if abs(freq1 - freq2) <= self.deviation_limit:
		return True
	else:
		return False
	

    def compare(self):
	"""		
	Do a simple comare of two files' mono frequencies
	We say the two songs are equal if they have less then 'limit' diffences
	"""
	
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
		# Right now we assume the lengths of the songs are the same
		i = 0

		# Go through the samples and check for diff. If diff += 1 errors
		while  i < len(f1_noise):
			if not self.equal(f1_noise[i], f2_noise[i]):
		         	errors += 1
			i += 1
		
		# We've broken out of the loop due \
		# to completion or error limit reached
		# ^Figure out which one
		
		if errors < limit:	
			print "MATCH {f1} {f2}\n".format(f1=self.f1.file_name, f2=self.f2.file_name)
			return True

