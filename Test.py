__author__ = 'christopherlyver'
from wavData import WavData

test = WavData('audio/excerpt0.wav')

test.get_frequencies()
print test[:10]

test.make_mono()
print test.frequencies[:10]