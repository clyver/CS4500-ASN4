author__ = 'christopherlyver'
import numpy as np
from numpy.fft import rfft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import pylab as pl
import pdb
import warnings

warnings.filterwarnings("ignore")

#pdb.set_trace()

class WavData():
    """
    Class contains the utilities needed to extract numerical data from WAV file
    """
    def __init__(self, wav_file):
        self.file_name = wav_file
        self.sample_rate, self.frequencies = wavfile.read(wav_file)
	self.duration = None

    def fft_to_freq(self, val):
	return abs(val * self.sample_rate)/100000    

    def short_name(self):
	# sometimes we'll want quick access to the file's short name, not path
	name_list = self.file_name.rsplit('/', 1)
	return name_list[1]
	
    def get_frequencies(self, listof_min_data):
        # Convert listof_min_data from rfft to hz
	listof_min_hz = []

	for x in listof_min_data:
		listof_min_hz.append(abs(x*self.sample_rate)/100000)

	return listof_min_hz
	
	
	
	
    def make_mono(self):
	# MUST ALWAYS EXECUTE BEFORE CALLING GET_FFT TO AVOID SIDE EFFECT CORRUPTION
	"""
	Take stereo data and make it into mono data
	"""

	mono_frequencies = []
        for sample in self.frequencies:
            # For each sample, average the stereo values
            left = sample[0]
            right = sample[1]
            mono_avg = (left + right) / 2

            mono_frequencies.append(mono_avg)
	

	self.frequencies = mono_frequencies

    def make_min_max_samples(self):
	# Create a list of min max amp values for each second of the wav data
	min_max = []

	seconds_list = [self.frequencies[x:x+44100] for x in range(0, len(self.frequencies),44100)]

	for second in seconds_list:
		for x in second:
			if (x >= 0):
				frame_min = x
			if (x < frame_min and x >= 0):
				frame_min = x
		frame_max = np.amax(second)

		min_max.append((frame_min, frame_max))

	# FOR TESTING PURPOSES
	#print min_max

	# Convert min_max from amps to freqs
	count = 0
	while(count < len(min_max)):
		# rfft the pair and convert to hz
		min_max[count] = (self.fft_to_freq(min_max[count][0]), self.fft_to_freq(min_max[count][1]))
		count += 1	
	self.frequencies = min_max
	#print self.frequencies

    def get_duration(self):
	"""
	Return the duration of the file in number of seconds
	"""
	samples = len(self.frequencies)
	sample_rate = self.sample_rate
	duration = samples/sample_rate
	
	self.duration = duration
