__author__ = 'christopherlyver'
from wavData import WavData
from compare import Compare

# A test to make sure our WavData is up to par
test = WavData('audio/excerpt0.wav')

test.get_frequencies()
print test.frequencies

print "************************************************************************"
# call fft on the freqs
test.get_fft()
for freq in test.frequencies:
	print freq

#A basic test to see that the same song is equal to itself
test2 = Compare('audio/excerpt0.wav', 'audio/excerpt0.wav', 50)
test2.naive_compare()
