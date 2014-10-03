__author__ = 'christopherlyver'
import numpy as np
from scipy.io import wavfile
import pdb

#pdb.set_trace()

# Wav audio files in our directory, taken from Clinger's audio samples.
file1 = 'wayfaring.wav'
file2 = 'excerpt0.wav'

# I've run into some trouble if I don't use Clinger's supplied wav files.
# ^Unsure why

# Read() returns a tuple (sample rate, data read from array)
sample_rate, stereo_data = wavfile.read(file2)

print sample_rate
# Data is a list of tuple lists, representing stero sound (left and right)
# Print out the first ten frequency samples
print stereo_data[:10]

