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

print "Two identical files that should match:"
test1 = Compare('audio/A4/z01.wav', 'audio/A4/z01.wav', 2.7,  1)
test1.compare()

print "Two diff files that should match:" 
test2 = Compare('audio/A4/z01.wav', 'audio/A4/z02.wav', 2.7, 1)
test2.compare()

print "Two diff files that should NOT match:" 
test3 = Compare('audio/A4/z02.wav', 'audio/A4/z03.wav', 2.7, 1)
test3.compare()

print "Two diff files that should match:" 
test4 = Compare('audio/A4/z03.wav', 'audio/A4/z04.wav', 672, 1)
test4.compare()

print "Two diff files that should NOT match:" 
test5 = Compare('audio/A4/z04.wav', 'audio/A4/z05.wav', 2.7, 1)
test5.compare()

print "Two diff files that should match:" 
test6 = Compare('audio/A4/z05.wav', 'audio/A4/z06.wav', 2.7, 1)
test6.compare()

print "Two diff files that should NOT match:" 
test7 = Compare('audio/A4/z06.wav', 'audio/A4/z07.wav', 2.7, 1)
test7.compare()

print "Two diff files that should match:" 
test8 = Compare('audio/A4/z07.wav', 'audio/A4/z08.wav', 2.7, 1)
test8.compare()

print "Two diff files that should NOT match:" 
test9 = Compare('audio/A4/z05.wav', 'audio/A4/Sor3508.wav', 2.7, 1)
test9.compare()


