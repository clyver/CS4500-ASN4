__author__ = 'christopherlyver'
import numpy as np
from numpy.fft import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import pylab as pl

#pdb.set_trace()

class WavData():
    """
    Class contains the utilities needed to extract numerical data from WAV file
    """
    def __init__(self, wav_file):
        self.file = wav_file
        self.frequencies = []
        self.sample_rate = None

    def get_frequencies(self):
        """
        Use wavfile.read() to get sample rate and stereo data from the wav file
        """
        sample_rate, data = wavfile.read(self.file)
        self.sample_rate = sample_rate
        self.frequencies = data
	


	p = 20*np.log10(np.abs(np.fft.rfft(data[:2048, 0])))
	f = np.linspace(0, sample_rate/2.0, len(p))
	pl.plot(f, p)
	pl.xlabel("Frequency(Hz)")
	pl.ylabel("Power(dB)")
	pl.show()
 	
	
	
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
	self.frequencies = fft(self.frequencies)
	data = self.frequencies


	


