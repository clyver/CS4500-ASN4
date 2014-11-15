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
	self.f1.get_duration()
	self.f1.make_mono()
	self.f1.make_min_max_samples()
			
	self.f2 =  WavData(f2)
	self.f2.get_duration()
	self.f2.make_mono()
	self.f2.make_min_max_samples()

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
		
		#print "f1_noise {f1}".format(f1 = f1_noise)
		#print "####################################"
		#print "f2_noise {f2}".format(f2 = f2_noise)
 
		# Right now we assume the lengths of the songs are the same

		ind0 = 0
		ind1 = 0
		# Go through the samples and check for diff. If diff += 1 errors
		for i in f1_noise:
			for j in i:
				# FOR TESTING PURPOSES
				#print "comparing {t1} with {t2}".format(t1=j, t2=f2_noise[ind0][ind1])
				if not self.equal(j, f2_noise[ind0][ind1]):
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
