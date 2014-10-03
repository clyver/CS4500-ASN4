__author__ = 'christopherlyver'
import numpy
from scipy.io import wavfile
import pdb

pdb.set_trace()
sample, data = wavfile.read("alrighty.wav")

print sample
print data[:5]

