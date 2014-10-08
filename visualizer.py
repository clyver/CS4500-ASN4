import matplotlib.pyplot as plt
from scipy.io import wavfile
import sys, wave
import numpy as np
from scipy import fftpack

# take wav file from cmd line
new_wav = sys.argv[1]
print new_wav

# open wav file
sample_rate, wav_data = wavfile.read(new_wav)

# open wav file into wave_read object
wave_read_data = wave.open(new_wav)

fft_data = np.fft.rfft(wav_data)
print fft_data

seconds = wave_read_data.getnframes() / sample_rate
print seconds

all_freqs = np.fft.fftfreq(len(fft_data))

idx = np.argmax(np.abs(fft_data)**2)
print idx
freqs_in_hertz = []
for f in fft_data:
	freqs_in_hertz.append(abs(f*sample_rate)/100000)
print freqs_in_hertz[:1000]

#  sample rate is 44100 samples per second
#  so lets see the whole .wav file by taking the number of 
#  seconds and multiplying that by 44100, to get the total
#  frames we should plot
plt.plot(wav_data[0:wave_read_data.getnframes()])
plt.ylabel("amplitude")
plt.xlabel("time")
plt.title(new_wav)
plt.show()

plt.plot(freqs_in_hertz)
plt.show()
