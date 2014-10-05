__author__ = 'christopherlyver'
import numpy as np
from scipy.io import wavfile
import pdb

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
        sample_rate, stereo_data = wavfile.read(self.file)
        self.sample_rate = sample_rate
        self.frequencies = stereo_data

    def make_mono(self):
        i = 0
        for sample in self.frequencies:
            # For each sample, average the stereo values
            left = sample[0]
            right = sample[1]
            mono_avg = (left + right) / 2

            self.frequencies[i] = mono_avg

            i += 1


