__author__ = 'christopherlyver'
from wavData import WavData
from compare import Compare

"""
# A test to make sure our WavData is up to par
test = WavData('audio/excerpt0.wav')

test.get_frequencies()
print test.frequencies[:10]

test.get_duration()
print test.duration

test.make_mono()
print test.frequencies[:10]

# call fft on the freqs
test.get_fft()
print test.frequencies[:10]
"""

print "Two identical files that should match:\n"
test2 = Compare('audio/A4/z01.wav', 'audio/A4/z01.wav', 10,  50)
test2.compare()

print "Two diff files that should match:\n" 
test4 = Compare('audio/A4/z01.wav', 'audio/A4/z02.wav', 10, 50)
test4.compare()

print "Two diff files that should NOT match:\n" 
test4 = Compare('audio/A4/z02.wav', 'audio/A4/z03.wav', 10, 50)
test4.compare()

print "Two diff files that should match:\n" 
test4 = Compare('audio/A4/z03.wav', 'audio/A4/z04.wav', 10, 50)
test4.compare()

print "Two diff files that should NOT match:\n" 
test4 = Compare('audio/A4/z04.wav', 'audio/A4/z05.wav', 10, 50)
test4.compare()

print "Two diff files that should match:\n" 
test4 = Compare('audio/A4/z05.wav', 'audio/A4/z06.wav', 10, 50)
test4.compare()

print "Two diff files that should NOT match:\n" 
test4 = Compare('audio/A4/z06.wav', 'audio/A4/z07.wav', 10, 50)
test4.compare()

print "Two diff files that should match:\n" 
test4 = Compare('audio/A4/z07.wav', 'audio/A4/z08.wav', 10, 50)
test4.compare()

print "Two diff files that should NOT match:\n" 
test4 = Compare('audio/A4/z05.wav', 'audio/A4/Sor3508.wav', 10, 50)
test4.compare()


