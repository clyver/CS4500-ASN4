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
        self.frequencies = []
        self.sample_rate = None
	self.duration = None

    def short_name(self):
	# sometimes we'll want quick access to the file's short name, not path
	name_list = self.file_name.rsplit('/', 1)
	return name_list[1]
	
    def get_frequencies(self):
        """
        Use wavfile.read() to get sample rate and stereo data from the wav file
        """
        sample_rate, data = wavfile.read(self.file_name)
        self.sample_rate = sample_rate
        self.frequencies = data
	
	
	
    def make_mono(self):
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

    def get_fft(self):
	# Create a list of 20 min values from the wav data
	count = 0
	min_list = []
	while(count < 20):
		# Grab min
		min_list.append(np.amin(self.frequencies))
		# Pop min off list
		where_min = np.where(self.frequencies==np.amin(self.frequencies))
		self.frequencies = np.delete(self.frequencies, where_min)
		count += 1	

	rfft_min_list = []
	for x in min_list:
		rfft_min_list.append(rfft([x]))
	print rfft_min_list

    def get_duration(self):
	"""
	Return the duration of the file in number of seconds
	"""
	samples = len(self.frequencies)
	sample_rate = self.sample_rate
	duration = samples/sample_rate
	
	self.duration = duration
