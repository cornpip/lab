import wave
import struct

import numpy as np
import matplotlib.pyplot as plt

fname = ".\WaveTest2.wav"
wav_file = wave.open(fname, "r")

framerate = float(wav_file.getframerate())
nframes = wav_file.getnframes()

time = np.arange(0, nframes/framerate, 1/framerate)
data = []
for i in range(0,nframes):
    waveData = wav_file.readframes(1)
    data.append(struct.unpack('h', waveData))

wav_file.close()

plt.plot(time, data)
plt.xlabel("times[s]")
plt.ylabel("data")
plt.xlim(0, 0.01)
plt.show()