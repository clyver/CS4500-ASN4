__author__ = 'christopherlyver'
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
	self.frequencies = rfft(self.frequencies)
	data = self.frequencies

    def get_duration(self):
	"""
	Return the duration of the file in number of seconds
	"""
	samples = len(self.frequencies)
	sample_rate = self.sample_rate
	duration = samples/sample_rate
	
	self.duration = duration



